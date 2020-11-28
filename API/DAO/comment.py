import psycopg2

from CollectorDB.dbconfig import pg_config


class CommentDAO:
    """
    This class contains all the methods that create or obtain comments from the database. This class is the base for the
    class commentsHandler.
    """
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllComment(self):
        """
        This method gets all comments from the database and then returns them to the handler.
        """
        cursor = self.conn.cursor()
        query = "Select * from comment as C order by C.comment_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCommentById(self, id):
        """
        This method searches the database for a comment with a matching parameter id. If a comment with a matching id
        is found the matching comment gets returned to the handler. If no comment is found then the method just returns
        None.
        """
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.comment_id=%s order by C.comment_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getContent(self, content):
        """
        This method executes a query which searches the database for all comments with the specific content. If no
        comments with a matching content are found then the method returns None. If comments are found
        with a matching content then they are grouped and returned.
        """
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.content=%s order by C.comment_id;"
        cursor.execute(query, (content,))
        result = cursor.fetchall()
        if result is None:
            return None
        return result

    def getCommentByDate(self, date):
        """
        This method executes a query which searches the database for all comments which where created in the
        parameter date. If no comments with a matching date are found then the method returns None. If comments are found
        with a matching date then they are grouped and returned.
        """
        cursor = self.conn.cursor()
        query = "Select * from comment as C where C.comment_date=%s order by C.comment_id;"
        cursor.execute(query, (date,))
        result = cursor.fetchall()
        if result is None:
            return None
        return result

    def insertComment(self, content, cDate, userID, threadID):
        """
        This method first receives several parameters, from the handler, as input. The method then executes the specific
        query which stores the given parameters in the database. Finally the method then fetches the id of the newly
        added user and returns it to the handler.
        """
        cursor = self.conn.cursor()
        query = "insert into comment(content, comment_Date, user_id, thread_id) values (%s, %s, %s, %s) " \
                "returning comment_id;"
        cursor.execute(query, (content, cDate, userID, threadID))
        result = cursor.fetchone()
        self.conn.commit()
        return result
