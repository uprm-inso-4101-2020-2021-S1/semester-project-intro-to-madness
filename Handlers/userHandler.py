from flask import jsonify
from DAO.user import UserDAO


class UserHandler:

    def build_user(self, row):
        result = {"ID": row[0], 'password': row[1], 'first_name': row[2], 'last_name': row[3], 'email': row[4],
                  'username': row[5],'role':row[6]}
        return result
    def build_user_attributes(self4param0,param0,param1,param2,param3,param4,param5,param6):
        result = {"ID": param0, 'first_name': param1, 'last_name': param2, 'username': param3, 'password':param4,
                  'email': param5,'role':param6}
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

    def createUser(self,args):
        param0 = args.get('ID')
        param1 = args.get('first_name')
        param2 = args.get('last_name')
        param3 = args.get('username')
        param4 = args.get('password')
        param5 = args.get('email')
        if param0 and param1 and param2 and param3 and param4 and param5:
            result = self.build_user_attributes(param0,param1,param2,param3,param4,param5)
            return jsonify(CreateStatus= result),201
        else:
            return jsonify(Error="Missing attributes in post request"),404

    def updateUser(self,ID,args):
        dao = UserDAO()
        if(dao.getUserById(ID)):
            param0 = args.get('ID')
            param1 = args.get('first_name')
            param2 = args.get('last_name')
            param3 = args.get('username')
            param4 = args.get('password')
            param5 = args.get('email')

            if(param0 !=ID):
                return jsonify(Error="User does not match"),400
            elif param0 and param1 and param2 and param3 and param4 and param5:
                result = self.build_user_attributes(param0,param1,param2,param3,param4,param5)
                return jsonify(UpdateStatus= result),201

            else:
                return jsonify(Error="Missing attributes in post request"), 404
        else:
            return jsonify(Error = "No User Found"),404

