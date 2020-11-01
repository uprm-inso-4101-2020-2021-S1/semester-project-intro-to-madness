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
        result = cursor.fetchall()
        return result

    def getDuplicateThreads(self):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.duplicate=%s order by T.thread_id;"
        cursor.execute(query, ("True",))
        result = cursor.fetchall()
        return result

    def getThreadsByCategory(self, category):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.category=%s order by T.thread_id;"
        cursor.execute(query, (category,))
        result = cursor.fetchall()
        return result

    def countThreads(self,ID):
        cursor = self.conn.cursor()
        query = " Select * from thread as T where T.category=%s order by T.thread_id;"
        cursor.execute(query, (ID,))
        result = cursor.fetchone()
        return result

    def getContentAndUsernameFromCommentsOnSpecificThread(self,ID):
        cursor = self.conn.cursor()
        query = " select content,username from comment as c natural inner join thread as t natural inner join users " \
                "as u where t.thread_id=%s and t.thread_id=c.thread_id and u.user_id=c.user_id;"
        cursor.execute(query, (ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSpecificItemThread(self, ID):
        cursor = self.conn.cursor()
        query = " select item_name, item_description, item_history, average_price, image_url, category from item " \
                "as i natural inner join thread as t where t.thread_id=%s and t.item_id=t.item_id;"
        cursor.execute(query, (ID,))
        result = cursor.fetchone()
        return result

    def getItemWithRelatedCategories(self, Category):
        cursor = self.conn.cursor()
        query = " select item_name, image_url, (select category FROM thread as t2 WHERE t.category = t2.category) " \
                "category from item as i natural inner join thread as t where t.thread_id=%s limit 3;"
        cursor.execute(query, (Category,))
        result = []
        for row in cursor:
            result.append(row)
        return result