from flask import jsonify
from DAO.thread import ThreadDAO


# Change mapped results
class threadHandler:

    def build_user(self, row):
        result = {"ID": row[0], 'Date': row[1], 'isDuplicate': row[2]}
        return result

    def getAllThreads(self):
        result = ThreadDAO().getAllThreads()
        mapped_result = []
        mapped_result = self.buildMethod(result)
        return mapped_result

    def getThreadByID(self, id):
        result = ThreadDAO().getThreadById(id)
        mapped_result = []
        if result is None:
            return None
        else:
            mapped_result.append(self.build_user(result))
        return mapped_result

    def getThreadsByDate(self, date):
        result = ThreadDAO().getThreadsByDate(date)
        mapped_result = self.buildMethod(result)
        return mapped_result

    def getAllDuplicateThreads(self):
        result = ThreadDAO().getDuplicateThreads()
        mapped_result = self.buildMethod(result)
        return mapped_result

    def buildMethod(self,result):
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_user(entry))
        return mapped_result
