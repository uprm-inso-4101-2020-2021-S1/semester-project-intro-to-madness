from flask import jsonify
from DAO.thread import ThreadDAO


# Change mapped results
class ThreadHandler:
    """
    This class is responsible for taking or sending data to and from the app routes. Data obtained from this class is
    sent over to the class threadDAO where it's managed according to the needs. Data obtained from the DAO is sent over
    to the appropriate route where it's displayed to the user.
    """
    # Build methods ------------------------------------------------------------------------------------------------

    def __build_thread(self, row):
        """
        This method is used by other methods in this class to properly format data. The method receives a row as a
        parameter and then splits the data into a dictionary. The dictionary is then returned to the corresponding method.
        """
        result = {"ID": row[0], 'Date': row[1], 'isDuplicate': row[2], 'Category': row[3], 'user_id': row[4]}
        return result

    def __build_thread_attributes(self, ID, date, duplicate, category, userID):
        """
        This method is used by other methods in this class to properly format data. The method receives several
        parameters and then splits the data into a dictionary. The dictionary is then returned to the corresponding
        method.
        """
        result = {"ID": ID, 'date': date, 'isDuplicate': duplicate, 'category': category, 'userID': userID}
        return result

    def __buildMethod(self, result):
        """
        This method is used by several methods to properly format all entries in an array. The method iterates over every
        row in the parameter result and then converts the iterated row into a dictionary. The dictionary is then entered
        mapped. Finally the mapped result is returned.
        """
        mapped_result = []
        for entry in result:
            mapped_result.append(self.__build_thread(entry))
        return mapped_result

    def createThread(self, json):
        """
        This method receives a json request from the app route. The method then splits the json into separate variables
        which are then given to the DAO to properly manage. The dao then returns an id corresponding to the assigned id
        given by the database. The data from the json along with the id are then returned in a json format.
        """
        date = json['date']
        duplicate = json['isDuplicate']
        category = json['category']
        user_id = json['user_ID']

        if date and duplicate and category:
            thread_id = ThreadDAO().inertThread(date, duplicate, category, user_id)
            result = self.__build_thread_attributes(thread_id, date, duplicate, category, user_id)
            return jsonify(Thread=result), 200
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400

    # Data access methods ----------------------------------------------------------------------------------

    def getAllThreads(self):
        """
        This method calls the method in the threadDAO responsible for retrieving all the threads from the database. The
        array of threads is then properly formatted and then converted into a json which is then returned.
        """
        result = ThreadDAO().getAllThreads()
        mapped_result = self.__buildMethod(result)
        return jsonify(Thread=mapped_result)

    def getThreadByID(self, id):
        """
        This method calls the method in threadDAO responsible for getting a thread by a parameter id. If no thread with
        a matching id is found the method returns a json containing an error message. If a thread with a matching id is
        found then its properly formatted and returned as a json.
        """
        result = ThreadDAO().getThreadById(id)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.__build_thread(result))
        return jsonify(Thread=mapped_result)

    def getAllDuplicateThreads(self):
        """
        This method calls the method in the DAO responsible for getting all duplicate threads. If no duplicate threads
        are found then the method returns a not found error in a json format. If duplicate threads are found the method
        iterates through every thread and formats them accordingly. Finally the formatted data is returned as a json.
        """
        result = ThreadDAO().getDuplicateThreads()
        mapped_result = self.__buildMethod(result)
        if len(mapped_result) == 0:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(Thread=mapped_result)

    def getThreadsBy(self, string):
        """
        This method receives a parameter as a string. The method begins by searching the string assuming its a date.
        If no results are found then the method searches by category. If both return None then the method returns a
        json containing a not found error.
        """
        try:
            result = ThreadDAO().getThreadsByDate(string)
            if len(result) > 0:
                mapped_result = self.__buildMethod(result)
                return jsonify(Thread=mapped_result)
        except:
            result = ThreadDAO().getThreadsByCategory(string)
            if len(result) > 0:
                mapped_result = self.__buildMethod(result)
                return jsonify(Thread=mapped_result)

        return jsonify(Error="Not Found"), 404

    def buildMethod(self, result):
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_thread(entry))
        return mapped_result

    def getThreadCount(self,ID):
        result = ThreadDAO().countThreads(ID)
        mapped_result = {"ThreadCount": result}
        return jsonify(Count=mapped_result),200

    def getContentAndUsernameFromCommentsOnSpecificThread(self,ID):
        result = ThreadDAO().getContentAndUsernameFromCommentsOnSpecificThread(ID)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        for entry in result:
            mapped_result.append(self.build_comments_from_users_on_a_specific_thread(entry))
        return jsonify(Thread=mapped_result)

    def getSpecificItemThread(self,ID):
        result = ThreadDAO().getSpecificItemThread(ID)
        mapped_result = self.build_item_thread(result)
        return jsonify(Thread=mapped_result)

    def getItemWithRelatedCategories(self, ID):
        result = ThreadDAO().getItemWithRelatedCategories(ID)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.build_item_with_related_category(result))
        return jsonify(Thread=mapped_result)
