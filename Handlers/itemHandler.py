from flask import jsonify
from DAO.item import ItemDAO


class ItemHandler:

    def build_item(self, row):
        result = {"ID": row[0], 'description': row[1], 'average_price': row[2], 'item_name': row[3], 'history': row[4],
                  'image_url': row[5]}
        return result

    def getAllItem(self):
        result = ItemDAO().getAllItem()
        mapped_result = []
        for entry in result:
            mapped_result.append(self.build_item(entry))
        return jsonify(User=mapped_result)

    def getItemByID(self, id):
        result = ItemDAO().getItemById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getItemDescription(self, description):
        result = ItemDAO().getItemDescription(description)
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getAveragePrice(self, price):
        result = ItemDAO().getAveragePrice(price)
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getItemName(self, name):
        result = ItemDAO().getItemName(name)
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getItemHistory(self, history):
        result = ItemDAO().getItemHistory(history)
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getItemImageURL(self, itemURL):
        result = ItemDAO().getImageUrl(itemURL)
        mapped_result = self.build_item(result)
        return jsonify(User=mapped_result)

    def getItemBy(self, string):
        result = ItemDAO().getItemDescription(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Thread=mapped_result)
        result = ItemDAO().getItemName(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Thread=mapped_result)
        result = ItemDAO().getItemHistory(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Thread=mapped_result)
        result = ItemDAO().getImageUrl(string)
        if result:
            mapped_result = self.build_item(result)
            return jsonify(Thread=mapped_result)
        else:
            return jsonify(Error="NOT FOUND"), 404
