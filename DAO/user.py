import psycopg2
from db.dbconfig import pg_config

class UserDAO:
    def __init__(self):
        self.data = []
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],pg_config['user'],pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "Select * from users as U order by U.user_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        query = "Select * from users as U where U.user_id = %s order by U.user_id;"
        cursor.execute(query,(id,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.email=%s order by U.user_id;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = " Select * from users as U where U.username=%s order by U.user_id;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if not result:
            return None
        return result





