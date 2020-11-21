from flask import jsonify
from DAO.item import ItemDAO


class ItemHandler:
    """
    This class is responsible for taking or sending data to and from the app routes. Data obtained from this class is
    sent over to the class ItemDAO where it's managed according to the needs. Data obtained from the DAO is sent over
    to the appropriate route where it's displayed to the user.
    """
    def build_item(self, row):
        """
        This method is used by other methods in this class to properly format data. The method receives a row as a
        parameter and then splits the data into a dictionary. The dictionary is then returned to the corresponding method.
        """
        result = {'ID': row[0], 'item_description': row[1], 'average_price': row[2], 'item_name': row[3],
                  'item_history': row[4], 'image_url': row[5]}
        return result

    def __build_item_attributes(self, ID, iDesc, iPrice, iName, iHistory, iImage, userID):
        """
        This method is used by other methods in this class to properly format data. The method receives several
        parameters and then splits the data into a dictionary. The dictionary is then returned to the corresponding
        method.
        """
        result = {"ID": ID, 'item_description': iDesc, 'average_price': iPrice, 'item_name': iName,
                  'item_history': iHistory, 'image_url': iImage, 'user_ID': userID}
        return result

    def createItem(self, json):
        """
        This method receives a json request from the app route. The method then splits the json into separate variables
        which are then given to the DAO to properly manage. The DAO then returns an id corresponding to the assigned id
        given by the database. The data from the json along with the id are then returned in a json format.
        """
        iDesc = json['item_description']
        iPrice = json['average_price']
        iName = json['item_name']
        iHistory = json['item_history']
        iImage = json['image_url']
        userID = json['user_ID']
        if iDesc and iPrice and iName and iHistory and iImage and userID:
            item_id = ItemDAO().insertItem(iDesc, iPrice, iName, iHistory, iImage, userID)
            result = self.__build_item_attributes(item_id, iDesc, iPrice, iName, iHistory, iImage, userID)
            return jsonify(User=result), 200
        else:
            return jsonify(Error="Unexpected attribute in post request"), 400

    def getAllItem(self):
        """
        This method calls the method in the ItemDAO responsible for retrieving all the items from the database. The
        array of items is then properly formatted and then converted into a json which is then returned.
        """
        result = ItemDAO().getAllItem()
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_item(entry))
        return jsonify(Item=mapped_result)

    def getItemByID(self, id):
        """
        This method calls the method in ItemDAO responsible for getting an items by a parameter id. If no items with
        a matching id is found the method returns a json containing an error message. If an item with a matching id is
        found then its properly formatted and returned as a json.
        """
        result = ItemDAO().getItemById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.build_item(result)
        return jsonify(Item=mapped_result)

    def getItemDescription(self, description):
        """
        This method calls the method in ItemDAO responsible for getting a item by a parameter description. If no item
        with a matching description is found the method returns a json containing an error message. If an item with a
        matching description is found then its properly formatted and returned as a json.
        """
        result = ItemDAO().getItemDescription(description)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getAveragePrice(self, price):
        """
        This method calls the method in the DAO responsible for getting all item with the average price. If no items
        are found then the method returns a not found error in a json format. If items are found the method
        iterates through every thread and formats them accordingly. Finally the formatted data is returned as a json.
        """
        result = ItemDAO().getAveragePrice(price)
        if result:
            mapped_result = []
            for entry in result:
                mapped_result.append(self.build_item(entry))
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getItemName(self, name):
        """
        This method calls the method in ItemDAO responsible for getting a item by a parameter name. If no item
        with a matching name is found the method returns a json containing an error message. If an item with a
        matching name is found then its properly formatted and returned as a json.
        """
        result = ItemDAO().getItemName(name)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getItemHistory(self, history):
        """
        This method calls the method in ItemDAO responsible for getting a item by a parameter history. If no item
        with a matching history is found the method returns a json containing an error message. If an item with a
        matching history is found then its properly formatted and returned as a json.
        """
        result = ItemDAO().getItemHistory(history)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getItemImageURL(self, itemURL):
        """
        This method calls the method in ItemDAO responsible for getting a item by a parameter itemURL. If no item
        with a matching itemURL is found the method returns a json containing an error message. If an item with a
        matching itemURL is found then its properly formatted and returned as a json.
        """
        result = ItemDAO().getImageUrl(itemURL)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404

    def getItemBy(self, string):
        """
        This method receives a parameter as a string. The method begins by searching the string assuming its a itemName.
        If no results are found then the method searches by averagePrice. If no results are found then the method
        searches by itemDescription. If no results are found then the method searches by itemHistory. If no results are
        found then the method searches by imageURL. If all return None then the method returns a json containing a not
        found error.
        """
        result = ItemDAO().getItemName(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        result = ItemDAO().getAveragePrice(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        result = ItemDAO().getItemDescription(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        result = ItemDAO().getItemHistory(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        result = ItemDAO().getImageUrl(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Item=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404