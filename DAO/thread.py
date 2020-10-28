import psycopg2
from CollectorDB.dbconfig import pg_config


class ThreadDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"%(pg_config['dbname'],pg_config['user'],pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllThreads(self):
        cursor = self.conn.cursor()
        query = "Select * from thread as T order by T.thread_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getThreadById(self, id):
        cursor = self.conn.cursor()
        query = "Select * from thread as T where T.thread_id=%s order by T.thread_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getThreadsByDate(self, date):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.thread_date=%s order by T.thread_id;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDuplicateThreads(self):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.duplicate=%s order by T.thread_id;"
        cursor.execute(query, ("True",))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getThreadsByCategory(self, category):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.category=%s order by T.thread_id;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result
