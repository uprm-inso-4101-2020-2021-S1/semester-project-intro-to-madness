# in order to run, type 'python -m flask run' in the command line
from Handlers.userHandler import UserHandler
from Handlers.threadHandler import ThreadHandler
from Handlers.commentHandler import CommentHandler
from Handlers.itemHandler import ItemHandler
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/users", methods=['GET'])
def getAllUsers():
    return UserHandler().getAllUsers()


@app.route("/users/activity/<int:ID>", methods=['GET'])
def getUserActivity(ID):
    return UserHandler().getUserActivity(ID)


@app.route("/users/register", methods=['POST'])
def Register():
    return UserHandler().createUser(request.json)


@app.route("/users/login", methods=['POST'])
def Login():
    return UserHandler().getUserByUsernameAndPassword(request.json)


@app.route("/users/<int:ID>", methods=['GET'])
def getUserByID(ID):
    return UserHandler().getUserInformation(ID)


@app.route("/users/<UserString>", methods=['GET'])
def getUserBy(UserString):
    return UserHandler().getUsersBy(UserString)


@app.route("/users/update/<int:ID>", methods=['PUT'])
def updateUser(ID):
    return UserHandler().updateUser(ID, request.json)


@app.route("/threads", methods=['GET'])
def getAllThreads():
    return ThreadHandler().getAllThreads()


@app.route("/threads/<int:threadID>", methods=['GET'])
def getThreadByID(threadID):
    return ThreadHandler().getThreadByID(threadID)


@app.route("/threads/<ThreadString>", methods=['GET'])
def getCategories(ThreadString):
    return ThreadHandler().getThreadsBy(ThreadString)


@app.route("/threads/count/<int:ID>", methods=['GET'])
def getThreadCount(ID):
    return ThreadHandler().getThreadCount(ID)


@app.route("/comment/thread/<int:ID>", methods=['GET'])
def getContentAndUsernameFromCommentsOnSpecificThread(ID):
    return ThreadHandler().getContentAndUsernameFromCommentsOnSpecificThread(ID)


@app.route("/threads/item/<int:ID>", methods=['GET'])
def getSpecificItemThread(ID):
    return ThreadHandler().getSpecificItemThread(ID)


@app.route("/category/thread/<int:ID>", methods=['GET'])
def getItemWithRelatedCategories(ID):
    return ThreadHandler().getItemWithRelatedCategories(ID)


@app.route("/threads/duplicates", methods=['GET'])
def getDuplicates():
    return ThreadHandler().getAllDuplicateThreads()


@app.route("/threads/create", methods=['Post'])
def createThread():
    return ThreadHandler().createThread(request.json)


@app.route("/comment", methods=['GET'])
def getAllComment():
    return CommentHandler().getAllComment()


@app.route("/comment/<int:ID>", methods=['GET'])
def getCommentByID(ID):
    return CommentHandler().getCommentByID(ID)


@app.route("/comment/date", methods=['GET'])
def getCommentByDate():
    return CommentHandler().getCommentByDate(request.json)


@app.route("/comment/create", methods=['Post'])
def createComment():
    return CommentHandler().createComment(request.json)


@app.route("/items", methods=['GET'])
def getAllItem():
    return ItemHandler().getAllItem()


@app.route("/items/<int:ID>", methods=['GET'])
def getItemByID(ID):
    return ItemHandler().getItemByID(ID)


@app.route("/items/price/<int:price>", methods=['GET'])
def getItemByAveragePrice(price):
    return ItemHandler().getAveragePrice(price)


@app.route("/items/<ItemString>", methods=['GET'])
def getItemBy(ItemString):
    return ItemHandler().getItemBy(ItemString)


@app.route("/items/create", methods=['Post'])
def createItem():
    return ItemHandler().createItem(request.json)


if __name__ == '__main__':
    app.run()
