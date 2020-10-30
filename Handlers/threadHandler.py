from flask import jsonify
from DAO.thread import ThreadDAO


# Change mapped results
class ThreadHandler:

    def build_thread(self, row):
        result = {"ID": row[0], 'Date': row[1], 'isDuplicate': row[2], 'Category': row[3],'user_id': row[4],'item_id': row[5]}
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

