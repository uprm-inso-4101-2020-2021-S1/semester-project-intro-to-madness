import psycopg2

from CollectorDB.dbconfig import pg_config


class ItemDAO:
    """
    This class contains all the methods that create or obtain items from the database. This class is the base for the
    class itemsHandler.
    """
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllItem(self):
        """
        This method gets all items from the database and then returns them to the handler.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I order by i.item_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getItemById(self, id):
        """
        This method searches the database for an item with a matching parameter id. If an item with a matching id
        is found the matching item gets returned to the handler. If no item is found then the method just returns
        None.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.item_id=%s order by i.item_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getItemDescription(self, description):
        """
        This method searches the database for an item with a matching parameter description. If an item with a matching description
        is found the matching item gets returned to the handler. If no item is found then the method just returns
        None.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.item_description=%s order by i.item_id;"
        cursor.execute(query, (description,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getAveragePrice(self, price):
        """
        This method executes a query which searches the database for all items which have the matching price from the
        parameter date. If no comments with a matching date are found then the method returns None. If comments are found
        with a matching date then they are grouped and returned.
        """
        cursor = self.conn.cursor()
        query = "Select item_id, item_description, average_price, item_name, item_history, " \
                "image_url, user_id from item as I natural inner join user_item as U where I.item_id=U.item_id " \
                "and I.average_price=%s;"
        cursor.execute(query, (price,))
        result = cursor.fetchone()
        if result is None:
            return None
        return result

    def getItemName(self, name):
        """
        This method searches the database for an item with a matching parameter name. If an item with a matching name
        is found the matching item gets returned to the handler. If no item is found then the method just returns None.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.item_name=%s order by i.item_id;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getItemHistory(self, history):
        """
        This method searches the database for an item with a matching parameter history. If an item with a matching history
        is found the matching item gets returned to the handler. If no item is found then the method just returns None.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I where I.item_history=%s order by i.item_id;"
        cursor.execute(query, (history,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getImageUrl(self, imageURL):
        """
        This method searches the database for an image with a matching parameter imageURL. If an image with a matching imageURL
        is found the matching image gets returned to the handler. If no image is found then the method just return None.
        """
        cursor = self.conn.cursor()
        query = "Select * from item as I where I.image_url=%s order by i.item_id;"
        cursor.execute(query, (imageURL,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def insertItem(self, iDesc, iPrice, iName, iHistory, iImage, userID):
        """
        This method first receives several parameters, from the handler, as input. The method then executes the specific
        query which stores the given parameters in the database. Finally the method then fetches the id of the newly
        added item and returns it to the handler.
        """
        cursor = self.conn.cursor()
        query = "insert into item(item_description, average_price, item_name, item_history, image_url, user_id) values " \
                "(%s, %s, %s, %s, %s, %s) returning item.item_id;"
        cursor.execute(query, (iDesc, iPrice, iName, iHistory, iImage, userID))
        result = cursor.fetchone()
        self.conn.commit()
        return result
