import flask
from flask import request, jsonify
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="abstractproject"
)

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/api/v1/get/users', methods=['GET'])
def getUsers():
    try:
        user = mydb.cursor()
        user.execute("SELECT * FROM user")
        allUsers = user.fetchall()
        return jsonify(allUsers)
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/create/user', methods=['GET', 'POST'])
def createUser():
    try:
        user = mydb.cursor()
        user.execute('''INSERT INTO user(name, email, password) VALUES (%s, %s,%s)''', (request.args.get('name'), request.args.get('email'), request.args.get('password')))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/one/user', methods=['GET', 'POST'])
def gechecktUsers():
    try:
        user = mydb.cursor()
        user.execute('''SELECT * FROM user WHERE password = %s and email = %s''', (request.args.get('password'),request.args.get('email')))
        oneUser = user.fetchone()
        return jsonify(oneUser)
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/book', methods=['GET', 'POST'])
def getAllBooks():
    try:
        book = mydb.cursor()
        book.execute('''SELECT * FROM book WHERE userId = %s''', (request.args.get("id"),))
        allBooks = book.fetchall()
        return jsonify(allBooks)
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/one/book', methods=['GET'])
def getOneBook():
    try:
        book = mydb.cursor()
        book.execute('''SELECT * FROM book WHERE bookId = %s''', (request.args.get('id'),))
        oneBooks = book.fetchone()
        return jsonify(oneBooks)
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/create/book', methods=['GET', 'POST'])
def createBook():
    try:
        book = mydb.cursor()
        book.execute('''INSERT INTO book(name, description, userId) VALUES (%s, %s,%s)''', (request.args.get('name'), request.args.get('description'), request.args.get('userId')))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/delete/book', methods=['GET', 'POST'])
def deleteBook():
    try:
        book = mydb.cursor()
        book.execute('''DELETE FROM book WHERE bookId = %s''', (request.args.get('id'),))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/edit/book', methods=['GET', 'POST'])
def editBook():
    try:
        book = mydb.cursor()
        book.execute('''UPDATE book SET name = %s, description = %s WHERE bookId = %s''', (request.args.get('name'),request.args.get('description'), request.args.get('id')))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

if __name__ == '__main__':
    app.run(port=105) #A method that runs the application server.