import psycopg2
from CollectorDB.dbconfig import pg_config


class UserDAO:
    def __init__(self):
        self.data = []
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        """
        This method gets all users from the database and then returns them to the handler.
        """
        cursor = self.conn.cursor()
        query = "Select * from users as U order by U.user_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        """
        This method searches the database for an user with a matching parameter id. If an user with a matching id
        is found the matching user gets returned to the handler. If no user is found then the method just returns
        None.
        """
        cursor = self.conn.cursor()
        query = "Select * from users as U where U.user_id = %s order by U.user_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getUserByEmail(self, email):
        """
        This method searches the database for an user with a matching parameter email. If an user with a matching email
        is found the matching user gets returned to the handler. If no user is found then the method just returns
        None.
        """
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.email=%s order by U.user_id;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getUserByUsername(self, username):
        """
        This method searches the database for an user with a matching parameter username. If an user with a matching
        username is found the matching user gets returned to the handler. If no user is found then the method just
        returns None.
        """
        cursor = self.conn.cursor()
        query = " Select * from users as U where U.username=%s order by U.user_id;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def insertUser(self, password, first_name, last_name, email, username, role):
        """
        This method first receives several parameters, from the handler, as input. The method then executes the specific
        query which stores the given parameters in the database. Finally the method then fetches the id of the newly
        added user and returns it to the handler.
        """
        cursor = self.conn.cursor()
        query = "insert into users(password,  first_name, last_name,email, username, role) values (%s, %s, %s, %s, " \
                "%s, %s) returning user_id; "
        cursor.execute(query, (password, first_name, last_name, email, username, role,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getUserByUsernameAndPassword(self, username, password):
        """
        This method searches the database for an user with a matching parameter username and password. If an user with the
        matching parameters is found the matching user gets returned to the handler.
        If no user is found then the method just returns None.
        """
        cursor = self.conn.cursor()
        query = "Select * from users as U where U.username = %s AND U.password = %s order by U.user_id;"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()
        if not result:
            return None
        else:
            return result

    def getUserInfo(self, id):
        """
        This method searches the database for a public user with a matching parameter id. If a public user with a matching
        id is found the matching public user gets returned to the handler. If no user is found then the method just
        returns None
        """
        cursor = self.conn.cursor()
        query = "select first_name, last_name, email, username, role from users as u where u.user_id=%s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            query = "select Count(*) from users as u natural inner join thread as t natural inner join item as i where "\
                        "u.user_id=%s; "
            cursor.execute(query, (id,))
            count = cursor.fetchone()
            if count is None:
                return result + (0,)
            else:
                return result + count
        else:
            return None

    def getUserActivity(self, ID):
        """
        This method is responsible gathering the first five threads made by the user with the parameter id. If the user
        has no activity then it returns None. If an user does have activity then the first five threads are returned.
        """
        cursor = self.conn.cursor()
        query = "select item_name, item_description, image_url from users as u natural inner join thread as t natural " \
                "inner join item as i where u.user_id=%s; "
        cursor.execute(query, (ID,))
        result = cursor.fetchmany(5)
        if not result:
            return None
        return result

    def updateUser(self,ID,firstname,lastname):
        """
        This method searches for an user with a matching ID. if an user with the matching ID is found then the user
        gets updated with the parameter first name and last name. The updated user is then returned.
        """
        cursor = self.conn.cursor()
        query = "update users set first_name=%s,last_name=%s where user_id=%s"
        cursor.execute(query,(firstname,lastname,ID,))
        self.conn.commit()
        return UserDAO().getUserById(ID)



