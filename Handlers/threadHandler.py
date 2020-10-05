from flask import jsonify
from DAO.thread import ThreadDAO


# Change mapped results
class ThreadHandler:

    def build_thread(self, row):
        result = {"ID": row[0], 'Date': row[1], 'Category': row[2], 'isDuplicate': row[3]}
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
        result = ThreadDAO().getThreadsByDate(string)
        if len(result) > 0:
            mapped_result = self.buildMethod(result)
            return jsonify(Thread=mapped_result)
        result = ThreadDAO().getThreadsByCategory(string)
        if len(result) > 0:
            mapped_result = self.buildMethod(result)
            return jsonify(Thread=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def buildMethod(self, result):
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_thread(entry))
        return mapped_result
