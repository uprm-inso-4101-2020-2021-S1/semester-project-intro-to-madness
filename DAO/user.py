class UserDAO:
    def __init__(self):
        self.data = []
       # ID/name/lastname/username/passowrd/email
        self.data.append([1, "Bob", "Ross", "BobR", "121", "email"])
        self.data.append([2, "Juan", "Hernandez", "JH", "147", "email2"])
        self.data.append([3, "Bill", "Bell", "BBell", "345", "email3"])
        self.data.append([4, "Jake", "Red", "JakeR", "457565", "email4"])

    def getAllUsers(self):
        return self.data

    def getUserById(self, id):
        for entry in self.data:
            if id.__eq__(entry[0]):
                return entry
            else:
                continue
        return None

    def getUserByEmail(self, email):
        for entry in self.data:
            if email.__eq__(entry[5]):
                return entry
            else:
                continue
        return None

    def getUserByUsername(self, username):
        for entry in self.data:
            if username.__eq__(entry[3]):
                return entry
            else:
                continue
        return None




