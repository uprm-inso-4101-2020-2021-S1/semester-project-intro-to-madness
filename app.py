# in order to run, type 'python -m flask run' in the command line
from Handlers.userHandler import userHandler
from Handlers.threadHandler import threadHandler
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/users", methods=['GET'])
def getAllUsers():
    return userHandler().getAllUsers()


@app.route("/users/<int:ID>", methods=['GET'])
def getUserByID(ID):
    return userHandler().getUserByID(ID)

@app.route("/users/<UserString>", methods=['GET'])
def getUserBy(UserString):
    return userHandler().getUsersBy(UserString)


@app.route("/threads", methods=['GET'])
def getAllThreads():
    return threadHandler().getAllThreads()


@app.route("/threads/<int:threadID>", methods=['GET'])
def getThreadByID(threadID):
    return threadHandler().getThreadByID(threadID)


@app.route("/threads/<ThreadString>", methods=['GET'])
def getCategories(ThreadString):
    return threadHandler().getThreadsBy(ThreadString)

@app.route("/threads/duplicates", methods=['GET'])
def getDuplicates():
    return threadHandler().getAllDuplicateThreads()


if __name__ == '__main__':
    app.run()
