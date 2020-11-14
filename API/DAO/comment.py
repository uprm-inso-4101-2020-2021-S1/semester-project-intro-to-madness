import psycopg2

from CollectorDB.dbconfig import pg_config


class CommentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllComment(self):
        cursor = self.conn.cursor()
        query = "Select * from comment as C order by C.comment_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCommentById(self, id):
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.comment_id=%s order by C.comment_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getContent(self, content):
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.content=%s order by C.comment_id;"
        cursor.execute(query, (content,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCommentByDate(self, date):
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.comment_date=%s order by C.comment_id;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
