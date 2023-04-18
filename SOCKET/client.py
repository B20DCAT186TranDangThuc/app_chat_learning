import socket
import sys 
import threading

class ClientNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.connect(port_and_ip)

    def send_sms(self, SMS):
        self.node.send(SMS.encode())

    def receive_sms(self):
        while True:       
            data = self.node.recv(1024).decode()
            if data =="quit: success":
                self.node.close()
                break
            print(data)

    def main(self):
        while True:
            message = input()
            if input == "5$$":
                self.node.close()
                sys.exit()
                break
            self.send_sms(message)

Client = ClientNode()
always_receive = threading.Thread(target=Client.receive_sms)
always_receive.daemon = True
always_receive.start()
Client.main()