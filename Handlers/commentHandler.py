from flask import jsonify
from DAO.comment import CommentDAO


# Change mapped results
class CommentHandler:

    def build_comment(self, row):
        result = {'comment_id': row[0], 'content': row[1], 'comment_date': row[2], 'user_id': row[3], 'thread_id': row[4]}
        return result

    def getAllComment(self):
        result = CommentDAO().getAllComment()
        mapped_result = self.buildMethod(result)
        return jsonify(Comment=mapped_result)

    def getCommentByID(self, id):
        result = CommentDAO().getCommentById(id)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.build_comment(result))
        return jsonify(Comment=mapped_result)

    def getCommentByDate(self, json):
        result = CommentDAO().getCommentByDate(json["comment_date"])
        mapped_result = self.buildMethod(result)
        return jsonify(Comment=mapped_result)

    def buildMethod(self, result):
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_comment(entry))
        return mapped_result
