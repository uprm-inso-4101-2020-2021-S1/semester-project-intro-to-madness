from flask import jsonify
from DAO.user import UserDAO


class userHandler:

    def build_user(self, row):
        result = {"ID": row[0], 'first_name': row[1], 'last_name': row[2], 'username': row[3], 'password': row[4],
                  'email': row[5]}
        return result

    def getAllUsers(self):
        result = UserDAO().getAllUsers()
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_user(entry))
        return mapped_result

    def getUserByID(self, id):
        result = UserDAO().getUserById(id)
        mapped_result = self.build_user(result)
        return mapped_result

    def getUserByEmail(self, email):
        result = UserDAO().getUserByEmail(email)
        mapped_result = self.build_user(result)
        return mapped_result

    def getUserByUsername(self, username):
        result = UserDAO().getUserByUsername(username)
        mapped_result = self.build_user(result)
        return mapped_result

    def getUserByFullName(self, first, last):
        result = UserDAO().getUserByFullName(first, last)
        mapped_result = self.build_user(result)
        return mapped_result

    def buildMethod(self,result):
        mapped_result = []
        if result is None:
            return None
        else:
            mapped_result.append(self.build_user(result))
        return mapped_result
