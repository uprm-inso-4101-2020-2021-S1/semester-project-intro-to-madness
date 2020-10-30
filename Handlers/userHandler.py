from flask import jsonify
from DAO.user import UserDAO


class UserHandler:

    # Data formatting ---------------------------------------------------------------------------------------

    def build_user(self, row):
        result = {"ID": row[0], 'password': row[1], 'first_name': row[2], 'last_name': row[3], 'email': row[4],
                  'username': row[5], 'role': row[6]}
        return result

    def build_user_attributes(self, ID,paswd , fname , lname , email , uname , role):
        result = {"ID": ID, 'password': paswd, 'first_name': fname, 'last_name': lname, 'email': email,
                  'username': uname, 'role': role}
        return result

    def build_public_user(self, row):
        result = {'first_name': row[0], 'last_name': row[1], 'email': row[2], 'username': row[3]}
        return result



    # Data Access ---------------------------------------------------------------------------------------

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

    def getUserInformation(self, ID):
        result = UserDAO().getUserInfo(ID)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.build_public_user(result)
        return jsonify(User=mapped_result)

    def getUserByUsernameAndPassword(self, json):
        username = json['username']
        password = json['password']
        result = UserDAO().getUserByUsernameAndPassword(username,password)
        if not result:
            return jsonify(Unauthorized="Incorrect username or password, please try again"), 401
        else:
            return jsonify(User=self.build_user(result)), 200

    # Register ---------------------------------------------------------------------------------------

    def createUser(self, json):
        pswd = json['password']
        fname = json['first_name']
        lname = json['last_name']
        email = json['email']
        uname = json['username']
        role = json['role']
        if pswd and fname and lname and email and uname and role:
            user_id = UserDAO().insertUser(pswd , fname , lname , email , uname , role)
            result = self.build_user_attributes(user_id,pswd , fname , lname , email , uname , role)
            return jsonify(User=result),200
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400
