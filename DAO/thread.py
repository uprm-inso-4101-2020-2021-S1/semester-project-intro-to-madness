import psycopg2
from CollectorDB.dbconfig import pg_config


class ThreadDAO:
    """
    This class contains all the methods that create or obtain threads from the database. This class is the base for the
    class threadHandler.
    """

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllThreads(self):
        """
        This method gets all threads from the database and then returns them to the handler.
        """

        cursor = self.conn.cursor()
        query = "Select * from thread as T order by T.thread_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getThreadById(self, id):
        """
        This method searches the database for a thread with a matching parameter id. If a thread with a matching id
        is found the matching thread gets returned to the handler. If no thread is found then the method just returns
        None.
        """

        cursor = self.conn.cursor()
        query = "Select * from thread as T where T.thread_id=%s order by T.thread_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getThreadsByDate(self, date):
        """
        This method executes a query which searches the database for all threads which where created in the
        parameter date. If no threads with a matching date are found then the method returns None. If threads are found
        with a matching date then they are grouped and returned.
        """

        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.thread_date=%s order by T.thread_id;"
        cursor.execute(query, (date,))
        result = cursor.fetchall()
        if result is None:
            return None
        return result

    def getDuplicateThreads(self):
        """
        This method executes a query which searches for all the threads in a database which are labeled as duplicate.
        The duplicate threads are grouped and then returned.
        """

        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.duplicate=%s order by T.thread_id;"
        cursor.execute(query, ("True",))
        result = cursor.fetchall()
        return result

    def getThreadsByCategory(self, category):
        """
        This method receives a category from the handler and then proceeds to execute a query which searches the database
        for all threads corresponding to the parameter category. All threads corresponding to the category are then
        returned to the handler.
        """

        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.category=%s order by T.thread_id;"
        cursor.execute(query, (category,))
        result = cursor.fetchall()
        return result

    def inertThread(self, date, duplicate, category, userID):
        """
        This method first receives several parameters, from the handler, as input. The method then executes the specific
        query which stores the given parameters in the database. Finally the method then fetches the id of the newly
        added thread and returns it to the handler.
        """

        cursor = self.conn.cursor()
        query = "select item_id from item ORDER BY item_id DESC LIMIT 1"
        cursor.execute(query)
        count = cursor.fetchone()
        item_id = int(''.join(map(str, count)))
        query = "insert into thread(thread_date,duplicate,category,user_id,item_id) values (%s, %s, %s,%s," \
                "%s) returning thread_id; "
        cursor.execute(query, (date, duplicate, category, userID, item_id,))
        result = cursor.fetchone()
        self.conn.commit()
        return result
