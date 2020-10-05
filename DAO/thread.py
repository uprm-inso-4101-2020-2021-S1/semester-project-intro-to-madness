
class ThreadDAO:
    def __init__(self):
        self.data = []
        self.data.append([1, "March 4,2020","coins",True])
        self.data.append([2, "September 6,1900","antiques",False])
        self.data.append([3, "September 6,1900","coins", False])
        self.data.append([4, "April 2, 1940","furniture",True])

    def getAllThreads(self):
        return self.data

    def getThreadById(self, id):
        for entry in self.data:
            if id.__eq__(entry[0]):
                return entry
            else:
                continue
        return None

    def getThreadsByDate(self, date):
        result = []
        for entry in self.data:
            if date.__eq__(entry[1]):
                result.append(entry)
            else:
                continue
        return result

    def getDuplicateThreads(self):
        result = []
        for entry in self.data:
            if entry[3].__eq__(True):
                result.append(entry)
            else:
                continue
        return result

    def getThreadsByCategory(self,category):
        result = []
        for entry in self.data:
            if entry[2].__eq__(category):
                result.append(entry)
            else:
                continue
        return result






