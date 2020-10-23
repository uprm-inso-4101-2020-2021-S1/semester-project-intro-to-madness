import psycopg2

from CollectorDB.dbconfig import pg_config


class ItemDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllItem(self):
        cursor = self.conn.cursor()
        query = "Select * from item as I order by i.i_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getItemById(self, id):
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.i_id=%s order by i.i_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getItemDescription(self, description):
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.item_description=%s order by i.i_id;"
        cursor.execute(query, (description,))
        result = cursor.fetchone()
        return result

    def getAveragePrice(self, item):
        cursor = self.conn.cursor()
        query = "Select average_price, item_id from item as I natural inner join user_item " \
                "as U where i.i_id=i.i_id and i.i_id=%s;"
        cursor.execute(query, (item,))
        result = cursor.fetchone()
        return result

    def getItemName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from item as I where i.item_name=%s order by i.i_id;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result

    def getItemHistory(self, history):
        cursor = self.conn.cursor()
        query = "Select * from item as I where I.item_history=%s order by i.i_id;"
        cursor.execute(query, (history,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getImageUrl(self, imageURL):
        cursor = self.conn.cursor()
        query = "Select * from item as I where I.image_url=%s order by i.i_id;"
        cursor.execute(query, (imageURL,))
        result = []
        for row in cursor:
            result.append(row)
        return result