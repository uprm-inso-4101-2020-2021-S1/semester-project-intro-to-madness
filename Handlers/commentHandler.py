from flask import jsonify
from DAO.comment import CommentDAO


# Change mapped results
class CommentHandler:

    def build_comment(self, row):
        result = {"ID": row[0], 'Content': row[1], 'Date': row[1]}
        return result

    def getAllComment(self):
        result = CommentDAO().getAllComment()
        mapped_result = self.buildMethod(result)
        return jsonify(Thread=mapped_result)

    def getCommentByID(self, id):
        result = CommentDAO().getCommentById(id)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.build_comment(result))
        return jsonify(Thread=mapped_result)

    def getCommentByDate(self, date):
        result = CommentDAO().getCommentByDate(date)
        mapped_result = self.buildMethod(result)
        return jsonify(Thread=mapped_result)

    def buildMethod(self, result):
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_comment(entry))
        return mapped_result
