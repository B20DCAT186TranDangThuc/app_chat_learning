import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def select_query(self, query, parameters=None):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def insert_query(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.connection.commit()

    def update_query(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.connection.commit()

    def delete_query(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.connection.commit()
# ------------------ những tính năng đi kèm để xử lý bên server ------------------
    def check_username(self, username):
        query = f"SELECT username FROM users WHERE username = '{username}';"
        results = self.select_query(query)
        if results:
            return True
        return False
    
    def add_user(self, username, password, fullname):
        query = 'INSERT INTO users (username, password, fullname) VALUES (%s, %s, %s)'
        self.insert_query(query, (username, password, fullname))

    def check_login(self, username, password):
        query = f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}';"
        results = self.select_query(query)
        if results:
            return True
        return False
    
    def get_user(self, username):
        query = f"SELECT user_id, username, fullname FROM users WHERE username = '{username}';"
        results = self.select_query(query)
        return results[0]

    def add_message(self, sender_id, receiver_id, message, time):
        query = 'INSERT INTO mesagers (sender_id, receiver_id, message_content, message_date) VALUES (%s, %s, %s, %s)'
        self.insert_query(query, (sender_id, receiver_id, message, time))

    def get_history(self, sender_id, receiver_id):
        query = f"SELECT * FROM mesagers WHERE (sender_id = {sender_id} AND receiver_id = {receiver_id}) OR (sender_id = {receiver_id} AND receiver_id = {sender_id}) ORDER BY message_date ASC;"
        results = self.select_query(query)
        return results
# # # Example usage:


# ---------------- test ----------------

# database = DatabaseConnector('127.0.0.1', 'root', '123456789', 'chatbox')
# database.connect()

# history = database.get_history(1, 2)
# for i in history:
#     print(i)
# database.add_message(2, 1, 'hello gi', '2021-05-01 11:00:00')

# username = "thucboykk"
# password = "11"

# query = f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}';"
# print(query)
# results = database.select_query(query)
# new_results = [item for sublist in results for item in sublist]
# print(new_results)
# Select query
# query = 'SELECT username, password FROM users;'
# results = database.select_query(query)
# for result in results:
#     print(result)

# Insert query
# for i in range(1, 10):
#     query = 'INSERT INTO user (id, user, password, fullname) VALUES (%s, %s, %s, %s)'
#     database.insert_query(query, (i, 'user' + str(i), 'password' + str(i), 'fullname' + str(i)))

# # Update query
# query = 'UPDATE users SET age = %s WHERE id = %s'
# database.update_query(query, (31, 1))

# # Delete query
# query = 'DELETE FROM users WHERE id = %s'
# database.delete_query(query, (1,))

# database.disconnect()
