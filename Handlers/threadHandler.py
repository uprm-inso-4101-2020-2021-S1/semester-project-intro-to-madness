from flask import jsonify
from DAO.thread import ThreadDAO


# Change mapped results
class ThreadHandler:

    def build_thread(self, row):
        result = {'thread_id': row[0], 'thread_date': row[1], 'duplicate': row[2], 'category': row[3],'user_id': row[4],'item_id': row[5]}
        return result

    def build_comments_from_users_on_a_specific_thread(self, row):
        result = {'content': row[0], 'username': row[1]}
        return result

    def build_item_thread(self, row):
        result = {'item_name': row[0], 'item_description': row[1], 'item_history': row[2], 'average_price': row[3], 'image_url': row[4], 'category': row[5]}
        return result

    def build_item_with_related_category(self, row):
        result = {'category_1': row[0], 'category_2': row[1], 'category_3': row[2]}
        return result

    def getAllThreads(self):
        result = ThreadDAO().getAllThreads()
        mapped_result = self.buildMethod(result)
        return jsonify(Thread=mapped_result)

    def getThreadByID(self, id):
        result = ThreadDAO().getThreadById(id)
        mapped_result = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result.append(self.build_thread(result))
        return jsonify(Thread=mapped_result)

    def getAllDuplicateThreads(self):
        result = ThreadDAO().getDuplicateThreads()
        mapped_result = self.buildMethod(result)
        if len(mapped_result) == 0:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(Thread=mapped_result)

    def getThreadsBy(self, string):
        result = "";
        try:
            result = ThreadDAO().getThreadsByDate(string)
        except:
           print()

        if len(result)>0:
            mapped_result = self.buildMethod(result)
            return jsonify(Thread=mapped_result)

        try:
            result = ThreadDAO().getThreadsByCategory(string)
        except:
            print()

        if len(result) > 0:
                mapped_result = self.buildMethod(result)
                return jsonify(Thread=mapped_result)

        return jsonify(Error="Not Found"),404

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
