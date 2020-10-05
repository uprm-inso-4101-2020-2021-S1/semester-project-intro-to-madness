from flask import jsonify
from DAO.user import UserDAO


class UserHandler:

    def build_user(self, row):
        result = {"ID": row[0], 'first_name': row[1], 'last_name': row[2], 'username': row[3], 'password': row[4],
                  'email': row[5]}
        return result

    def getAllUsers(self):
        result = UserDAO().getAllUsers()
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_user(entry))
        return jsonify(User=mapped_result)

    def getUserByID(self, id):
        result = UserDAO().getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.build_user(result)
        return jsonify(User=mapped_result)

    def getUserByEmail(self, email):
        result = UserDAO().getUserByEmail(email)
        mapped_result = self.build_user(result)
        return jsonify(User=mapped_result)

    def getUserByUsername(self, username):
        result = UserDAO().getUserByUsername(username)
        mapped_result = self.build_user(result)
        return jsonify(User=mapped_result)

    def getUsersBy(self, string):
        result = UserDAO().getUserByEmail(string)
        if result:
            mapped_result = self.build_user(result)
            return jsonify(Thread=mapped_result)
        result = UserDAO().getUserByUsername(string)
        if result:
            mapped_result = self.build_user(result)
            return jsonify(Thread=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404
