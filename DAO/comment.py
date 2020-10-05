class CommentDAO:
    def __init__(self):
        self.data = []
        self.data.append([1, "Hi.", "March 4,2020"])
        self.data.append([2, "Bye.", "September 6,1900"])
        self.data.append([3, "Wut up.", "September 6,1900"])
        self.data.append([4, "Peace out.", "April 2, 1940"])

    def getAllComment(self):
        return self.data

    def getCommentById(self, id):
        for entry in self.data:
            if id.__eq__(entry[0]):
                return entry
            else:
                continue
        return None

    def getContent(self, content):
        for entry in self.data:
            if content.__eq__(entry[1]):
                return entry
            else:
                continue
        return None

    def getCommentByDate(self, date):
        result = []
        for entry in self.data:
            if date.__eq__(entry[2]):
                result.append(entry)
            else:
                continue
        return result
