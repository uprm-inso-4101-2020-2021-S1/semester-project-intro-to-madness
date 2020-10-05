class ItemDAO:
    def __init__(self):
        self.data = []
        self.data.append([1, "pretty", 9293, "dimond", "Found it on the floor.", "pic"])
        self.data.append([2, "ugly", 273, "hair", "My hair.", "pic1"])
        self.data.append([3, "meh", 1, "stick", "Dog found it.", "pic2"])
        self.data.append([4, "uhhh", 3398, "robot", "Made it in 2 days.getAveragePrice", "pic3"])

    def getAllItem(self):
        return self.data

    def getItemById(self, id):
        for entry in self.data:
            if id.__eq__(entry[0]):
                return entry
            else:
                continue
        return None

    def getItemDescription(self, description):
        for entry in self.data:
            if description.__eq__(entry[1]):
                return entry
            else:
                continue
        return None

    def getAveragePrice(self, item):
        for entry in self.data:
            if item.__eq__(entry[2]):
                return entry
            else:
                continue
        return None

    def getItemName(self, name):
        for entry in self.data:
            if name.__eq__(entry[3]):
                return entry
            else:
                continue
        return None

    def getItemHistory(self, history):
        for entry in self.data:
            if history.__eq__(entry[4]):
                return entry
            else:
                continue
        return None

    def getImageUrl(self, imageURL):
        for entry in self.data:
            if imageURL.__eq__(entry[5]):
                return entry
            else:
                continue
        return None