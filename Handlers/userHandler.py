from flask import jsonify
from DAO.user import UserDAO


class UserHandler:

    def build_user(self, row):
        result = {"ID": row[0], 'password': row[1], 'first_name': row[2], 'last_name': row[3], 'email': row[4],
                  'username': row[5], 'role': row[6]}
        return result

    def build_user_attributes(self, ID, param1, param2, param3, param4, param5, param6, param7):
        result = {"ID": ID, 'password': param1, 'first_name': param2, 'last_name': param3, 'email': param4,
                  'username': param5, 'role': param6}
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

    def getUserByUsernameAndPassword(self,json):
        username = json['username']
        password = json['password']
        result = UserDAO.getUserByUsernameAndPAssword(username,password)
        if not result:
            return jsonify(Unauthorized ="Incorrect username or password, please try again"),401
        else:
            return jsonify(User=self.build_user(result)),200

    def createUser(self, json):
        param1 = json['ID']
        param2 = json['password']
        param3 = json['first_name']
        param4 = json['last_name']
        param5 = json['email']
        param6 = json['username']
        param7 = json['role']
        if param1 and param2 and param3 and param4 and param5 and param6 and param7:
            user = UserDAO.insertUser(param1, param2, param3, param4, param5, param6.param7)
            return jsonify(
                User=self.build_user_attributes(user, param1, param2, param3, param4, param5, param6, param7))
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400
