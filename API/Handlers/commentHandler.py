from flask import jsonify
from DAO.comment import CommentDAO


# Change mapped results
class CommentHandler:
    """
    This class is responsible for taking or sending data to and from the app routes. Data obtained from this class is
    sent over to the class CommentDAO where it's managed according to the needs. Data obtained from the DAO is sent over
    to the appropriate route where it's displayed to the user.
    """
    def build_comment(self, row):
        """
        This method is used by other methods in this class to properly format data. The method receives a row as a
        parameter and then splits the data into a dictionary. The dictionary is then returned to the corresponding method.
        """
        result = {'comment_id': row[0], 'content': row[1], 'comment_date': row[2], 'user_id': row[3], 'thread_id': row[4]}
        return result

    def __build_comment_attributes(self, ID, content, cDate, userID, threadID):
        """
        This method is used by other methods in this class to properly format data. The method receives several
        parameters and then splits the data into a dictionary. The dictionary is then returned to the corresponding
        method.
        """
        result = {"ID": ID, 'content': content, 'comment_date': cDate, 'user_id': userID,
                  'thread_id': threadID}
        return result

    def createComment(self, json):
        """
        This method receives a json request from the app route. The method then splits the json into separate variables
        which are then given to the DAO to properly manage. The DAO then returns an id corresponding to the assigned id
        given by the database. The data from the json along with the id are then returned in a json format.
        """
        content = json['content']
        cDate = json['comment_date']
        userID = json['user_id']
        threadID = json['thread_id']
        if content and cDate and threadID:
            comment_id = CommentDAO().insertComment(content, cDate, userID, threadID)
            result = self.__build_comment_attributes(comment_id, content, cDate, userID, threadID)
            return jsonify(User=result), 200
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400

    def getAllComment(self):
        """
        This method calls the method in the CommentDAO responsible for retrieving all the comments from the database.
        The array of comments is then properly formatted and then converted into a json which is then returned.
        """
        result = CommentDAO().getAllComment()
        mapped_result = self.buildMethod(result)
        return jsonify(Comment=mapped_result)

    def getCommentByID(self, id):
        """
        This method calls the method in CommentDAO responsible for getting a comments by a parameter id. If no comments
        with a matching id is found the method returns a json containing an error message. If a comment with a matching
        id is found then its properly formatted and returned as a json.
        """
        result = CommentDAO().getCommentById(id)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.build_comment(result))
        return jsonify(Comment=mapped_result)

    def getCommentByDate(self, json):
        """
        This method calls the method in CommentDAO responsible for getting a comments by a parameter date. If no comments
        with a matching date is found the method returns a json containing an error message. If a comment with a matching
        id is found then its properly formatted and returned as a json.
        """
        result = CommentDAO().getCommentByDate(json["comment_date"])
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.buildMethod(result)
        return jsonify(Comment=mapped_result)

    def buildMethod(self, result):
        """
        This method is used by several methods to properly format all entries in an array. The method iterates over every
        row in the parameter result and then converts the iterated row into a dictionary. The dictionary is then entered
        mapped. Finally the mapped result is returned.
        """
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_comment(entry))
        return mapped_result
