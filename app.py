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


@app.route("/users/register", methods=['POST'])
def Register():
    return UserHandler().createUser(request.json)


@app.route("/users/login", methods=['POST'])
def Login():
    return UserHandler().getUserByUsernameAndPassword(request.json)


@app.route("/users/<int:ID>", methods=['GET'])
def getUserByID(ID):
    return UserHandler().getUserByID(ID)


@app.route("/users/<UserString>", methods=['GET'])
def getUserBy(UserString):
    return UserHandler().getUsersBy(UserString)


@app.route("/threads", methods=['GET'])
def getAllThreads():
    return ThreadHandler().getAllThreads()


@app.route("/threads/<int:threadID>", methods=['GET'])
def getThreadByID(threadID):
    return ThreadHandler().getThreadByID(threadID)


@app.route("/threads/<ThreadString>", methods=['GET'])
def getCategories(ThreadString):
    return ThreadHandler().getThreadsBy(ThreadString)


@app.route("/threads/duplicates", methods=['GET'])
def getDuplicates():
    return ThreadHandler().getAllDuplicateThreads()


@app.route("/comment", methods=['GET'])
def getAllComment():
    return CommentHandler().getAllComment()


@app.route("/comment/<int:ID>", methods=['GET'])
def getCommentByID(ID):
    return CommentHandler().getCommentByID(ID)


@app.route("/comment/date", methods=['GET'])
def getCommentByDate():
    return CommentHandler().getCommentByDate(request.json)


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


if __name__ == '__main__':
    app.run()
