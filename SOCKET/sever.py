import socket
import threading
import DATABASE.connect as db
import time # thư viện thời gian

class ServerNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345) # Cổng và địa chỉ IP của server
        self.node.bind(port_and_ip) # Gắn cổng và địa chỉ IP cho server
        self.node.listen(5) # Chỉ chấp nhận 5 kết nối đồng thời
        self.connections = {} # Lưu danh sách các kết nối đến các client

        # Kết nối đến database
        self.database = db.DatabaseConnector('127.0.0.1', 'root', '123456789', 'chatbox')
        self.database.connect()

        # Dữ liệu định dạng mã kí tự
        self.encoding = 'utf-8'

        # Mã kí tự tương ứng với các chức năng
        self.request_register = '1' # Đăng ký tài khoản
        self.request_login = '2' # Đăng nhập
        self.request_send_message = '3' # Gửi tin nhắn
        self.request_find_member = '8' # Tìm kiếm thành viên
        self.request_quit = '5' # Thoát
        self.request_show_history = '6' # Xem lịch sử
        self.logout = '7' # Đăng xuất

    def start(self):
        while True:
            # Chấp nhận kết nối từ client và lưu lại kết nối đó vào danh sách
            conn, addr = self.node.accept()
            print(f"Connected to client: {addr}")
            self.connections[addr] = None

            # Xử lý kết nối và tin nhắn của client
            thread = threading.Thread(target=self.handle_connection, args=(conn, addr))
            thread.daemon = True
            thread.start()

    def handle_connection(self, connection, address):
        while True:
            try:
                # Nhận tin nhắn từ client
                data = connection.recv(1024).decode(self.encoding)
                print(data)
                # tách tin nhắn thành các phần theo $$ để lấy mã kí tự và nội dung
                data = data.split('$$')
                request = data[0] # Mã kí tự
                content = data[1] # Nội dung
                if request == self.request_register:
                    self.register(connection, address, content)
                elif request == self.request_login:
                    self.login(connection, address, content)
                elif request == self.request_send_message:
                    self.send_message(connection, address, content)
                elif request == self.request_find_member:
                    self.find_member(connection, address, content)
                elif request == self.request_quit:
                    self.quit(connection, address, content)
                elif request == self.request_show_history:
                    self.show_history(connection, address, content)
                elif request == self.logout:
                    self.logout(connection, address, content)
            except Exception as e:
                print(f"{address} disconnected")
                connection.close()
                break
        
    def register(self, connection, address, content):
        # content là thông tin đăng ký của client: username__password__fullname
        # tách thông tin đăng ký thành các phần theo __ để lấy username, password, fullname
        content = content.split('__')
        username = content[0]
        password = content[1]
        fullname = content[2]
        # Kiểm tra username đã tồn tại chưa
        if self.database.check_username(username):
            connection.send('register: fail'.encode(self.encoding))
            print(f"Username {username} already exists")
        else:
            # Thêm thông tin đăng ký vào database
            self.database.add_user(username, password, fullname)
            connection.send('register: success'.encode(self.encoding))
            print(f"Register {username} successfully")

    def login(self, connection, address, content):
        # content là thông tin đăng nhập của client: username__password
        # tách thông tin đăng nhập thành các phần theo __ để lấy username, password
        content = content.split('__')
        username = content[0]
        password = content[1]
        # Kiểm tra username và password có đúng không
        if self.database.check_login(username, password):
            connection.send('login: success'.encode(self.encoding))
            print(f"Login {username} successfully")
            # Lưu lại kết nối của client
            self.connections[connection] = username
        else:
            connection.send('login: fail'.encode(self.encoding))
            print(f"Login {username} failed")

    def send_message(self, connection, address, content):
        # content là thông tin tin nhắn của client: username__message
        # tách thông tin tin nhắn thành các phần theo __ để lấy username, message
        content = content.split('__')
        username = content[0]
        message = content[1]
        # Lấy id của người gửi và người nhận từ database
        sender_id = self.call_user_for_database(self.connections[connection])[0]
        receiver_id = self.call_user_for_database(username)[0]
        # Thêm tin nhắn vào database có cả time
        self.database.add_message(sender_id, receiver_id, message, time.strftime("%Y-%m-%d %H:%M:%S"))
        # gửi tin nhắn đến client kia nếu đang online
        for conn, user in self.connections.items():
            if user == username:
                conn.send(f"message: {self.connections[connection]}: {message}".encode(self.encoding))
                break
        # gửi thông điệp thành công đến client
        connection.send('send_message: success'.encode(self.encoding))
        print(f"{self.connections[connection]} sent message to {username}: {message}")
    def find_member(self, connection, address, content):
        print(f"Finding member: {content}")
        list_member = self.database.get_list_member(content)
        for member in list_member:
            print(member)
        # gửi thông báo tìm kiếm thành công đến client
        connection.send('find_member: success'.encode(self.encoding))

    def quit(self, connection, address, content):
        print(f"Quitting: {connection.getpeername()}") #getpeername() trả về địa chỉ IP và cổng của client
        connection.send('quit: success'.encode(self.encoding))
        connection.close()

    def show_history(self, connection, address, content):
        # content là thông tin lịch sử của client: username
        # Lấy id của người gửi và người nhận từ database
        sender_id = self.call_user_for_database(self.connections[connection])[0]
        receiver_id = self.call_user_for_database(content)[0]
        # Lấy lịch sử từ database
        history = self.database.get_history(sender_id, receiver_id)
        # Gửi lịch sử đến client
        connection.send(f"history: {history}".encode(self.encoding))
        print(f"Showing history of {self.connections[connection]} and {content}")
    
    def logout(self, connection, address, content):
        # chỉ xóa tên người dùng trong danh sách kết nối
        self.connections[connection] = None
        connection.send('logout: success'.encode(self.encoding))

    def call_user_for_database(self, username):
        # Lấy thông tin của username từ database
        return self.database.get_user(username)
    

server = ServerNode()
server.start()
