from flask import jsonify
from DAO.user import UserDAO


class UserHandler:
    """
    This class is responsible for taking or sending data to and from the app routes. Data obtained from this class is
    sent over to the class userDAO where it's managed according to the needs. Data obtained from the DAO is sent over
    to the appropriate route where it's displayed to the user.
    """
    # Build Methods---------------------------------------------------------------------------------------

    def __build_user(self, row):
        """
        This method is used by other methods in this class to properly format data. The method receives a row as a
        parameter and then formats the data into either a public user, which is seen by everyone, or a private user, which
        is only seen by the other code.
        """
        try:
            result = {"ID": row[0], 'password': row[1], 'first_name': row[2], 'last_name': row[3], 'email': row[4],
                      'username': row[5], 'role': row[6]}
        except:
            result = {'first_name': row[0], 'last_name': row[1], 'email': row[2], 'username': row[3],
                      'thread_count': row[5]}
        return result

    def __build_user_attributes(self, ID, paswd, fname, lname, email, uname, role):
        """
        This method is used by other methods in this class to properly format data. The method receives several
        parameters and then splits the data into a dictionary. The dictionary is then returned to the corresponding
        method.
        """
        result = {"ID": ID, 'password': paswd, 'first_name': fname, 'last_name': lname, 'email': email,
                  'username': uname, 'role': role}
        return result

    def __build_user_Activity(self,row):
        """
        This method receives a parameter row containing all user activity. The method then formats the data into a
        dictionary and then returns it.
        """
        result = {'Category': row[0], 'Description': row[1], 'ImageURl': row[2]}
        return result

    # Data Access ---------------------------------------------------------------------------------------

    def getAllUsers(self):
        """
        This method calls the method in the userDAO responsible for retrieving all the users from the database. The
        array of users is then properly formatted and then converted into a json which is then returned.
        """
        result = UserDAO().getAllUsers()
        mapped_result = []
        for entry in result:
            mapped_result.append(self.__build_user(entry))
        return jsonify(User=mapped_result)

    def getUserByID(self, id):
        """
        This method calls the method in userDAO responsible for getting an user by a parameter id. If no users with
        a matching id is found the method returns a json containing an error message. If an user with a matching id is
        found then its properly formatted and returned as a json.
        """
        result = UserDAO().getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.__build_user(result)
        return jsonify(User=mapped_result)

    def getUsersBy(self, string):
        """
        This method receives a parameter as a string. The method begins by searching the string assuming its an email.
        If no results are found then the method searches by username. If both return None then the method returns a
        json containing a not found error.
        """
        result = UserDAO().getUserByEmail(string)
        if result:
            mapped_result = self.__build_user(result)
            return jsonify(Thread=mapped_result)
        result = UserDAO().getUserByUsername(string)
        if result:
            mapped_result = self.__build_user(result)
            return jsonify(Thread=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getUserInformation(self, ID):
        """
        This method calls the method in userDAO responsible for getting a public user by a parameter id. If no users with
        a matching id is found the method returns a json containing an error message. If an user with a matching id is
        found then its properly formatted and returned as a json.
        """
        result = UserDAO().getUserInfo(ID)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.__build_user(result)
        return jsonify(User=mapped_result)

    def getUserActivity(self,ID):
        """
        This method receives an user ID as a parameter. The method then calls the appropriate method in the class userDAO
        responsible for gathering the firs five threads the user created. The threads are then formatted and returned
        as a json.
        """
        result = UserDAO().getUserActivity(ID)
        if result is None:
            return jsonify(Error="User has no Activity"), 404
        mapped_result = []
        for entry in result:
            mapped_result.append(self.__build_user_Activity(entry))
        return jsonify(Activity=mapped_result), 200

    # Register ---------------------------------------------------------------------------------------

    def createUser(self, json):
        """
        This method receives a json request from the app route. The method then splits the json into separate variables
        which are then given to the DAO to properly manage. The dao then returns an id corresponding to the assigned id
        given by the database. The data from the json along with the id are then returned in a json format.
        """
        pswd = json['password']
        fname = json['first_name']
        lname = json['last_name']
        email = json['email']
        uname = json['username']
        role = json['role']
        if pswd and fname and lname and email and uname and role:
            user_id = UserDAO().insertUser(pswd, fname, lname, email, uname, role)
            result = self.__build_user_attributes(user_id, pswd, fname, lname, email, uname, role)
            return jsonify(User=result), 200
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400

    # Update ---------------------------------------------------------------------------------------
    def updateUser(self,ID,json):
        """
        This method calls the method in the DAO responsible for updating the user with the matching parameter ID. The
        method then returns the updated user as a json.
        """
        firstname = json['first_name']
        lastname = json['last_name']
        result = UserDAO().updateUser(ID,firstname,lastname)
        if not result:
            return jsonify(Error="User Not Found"), 404
        else:
            return jsonify(User=self.__build_user(result)), 200

    # Login ---------------------------------------------------------------------------------------
    def getUserByUsernameAndPassword(self, json):
        """
        This receives a json as an input. THe method then calls the appropriate method in the DAo with the formatted json,
        The dao then checks to see if an user with matching username and password are found. If no user is found or the
        username and password are incorrect then it returns an error as a json. If an  user is found then the method returns
        the user as a json,
        """
        username = json['username']
        password = json['password']
        result = UserDAO().getUserByUsernameAndPassword(username, password)
        if not result:
            return jsonify(Unauthorized="Incorrect username or password, please try again"), 401
        else:
            return jsonify(User=self.__build_user(result)), 200
