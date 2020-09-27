class ThreadDAO:
    def __init__(self):
        self.data = []
        self.data.append([1, "03/15/2020", False])
        self.data.append([2, "04/20/2020",False])
        self.data.append([3, "04/21/2020", False])
        self.data.append([4, "04/21/2020",True])

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
            if entry[2].__eq__(True):
                result.append(entry)
            else:
                continue
        return result





