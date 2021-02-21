import flask
from flask import request, jsonify
import mysql.connector
import jwt
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="abstractproject"
)

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'RandomString'
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

@app.route('/api/v1/create/user', methods=['POST'])
def createUser():
    try:
        user = mydb.cursor()
        user.execute('''INSERT INTO user(name, email, password) VALUES (%s, %s,%s)''', (request.args.get('name'), request.args.get('email'), request.args.get('password')))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/one/user', methods=['GET'])
def gechecktUsers():
    try:
        user = mydb.cursor()
        user.execute('''SELECT * FROM user WHERE password = %s and email = %s''', (request.args.get('password'),request.args.get('email')))
        oneUser = user.fetchone()
        return jsonify(oneUser)
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/book/<id>', methods=['GET'])
def getAllBooks(id):
    try:
        if 'x-access-tokens' in request.headers:
            headers = request.headers.get('x-access-tokens')
            decodeToken = jwt.decode(headers , app.config['SECRET_KEY'])

            if decodeToken['mod'] == 'normal' or decodeToken['mod'] == 'readonly':
                book = mydb.cursor()
                book.execute('''SELECT * FROM book WHERE userId = %s''', (id,))
                allBooks = book.fetchall()
                return jsonify(allBooks)
            else:
                return 'false'
        else:
            return 'false'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/get/one/book/<id>', methods=['GET'])
def getOneBook(id):
    try:
        if 'x-access-tokens' in request.headers:
            headers = request.headers.get('x-access-tokens')
            decodeToken = jwt.decode(headers , app.config['SECRET_KEY'])
            
            if decodeToken['mod'] == 'normal':
                book = mydb.cursor()
                book.execute('''SELECT * FROM book WHERE bookId = %s''', (id,))
                oneBooks = book.fetchone()
                return jsonify(oneBooks)
            else:
                return 'false'
        else:
            return 'false'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/create/book', methods=['POST'])
def createBook():
    try:
        if 'x-access-tokens' in request.headers:
            headers = request.headers.get('x-access-tokens')
            decodeToken = jwt.decode(headers , app.config['SECRET_KEY'])
            
            if decodeToken['mod'] == 'normal':
                
                book = mydb.cursor()
                book.execute('''INSERT INTO book(name, description, userId) VALUES (%s, %s,%s)''', (request.args.get('name'), request.args.get('description'), request.args.get('userId')))
                mydb.commit()
                return 'true'
            else:
                return 'false'
        else:
            return 'false'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/delete/book/<id>', methods=['DELETE'])
def deleteBook(id):
    try:
        if 'x-access-tokens' in request.headers:
            headers = request.headers.get('x-access-tokens')
            decodeToken = jwt.decode(headers , app.config['SECRET_KEY'])
            
            if decodeToken['mod'] == 'normal':
                book = mydb.cursor()
                book.execute('''DELETE FROM book WHERE bookId = %s''', (id,))
                mydb.commit()
                return 'true'
            return 'false'
        else:
            return 'false'
    except mysql.connector.Error as error:
        print(error)

@app.route('/api/v1/edit/book/<id>', methods=['PUT'])
def editBook(id):
    try:
        book = mydb.cursor()
        book.execute('''UPDATE book SET name = %s, description = %s WHERE bookId = %s''', (request.args.get('name'),request.args.get('description'), id))
        mydb.commit()
        return 'true'
    except mysql.connector.Error as error:
        print(error)

if __name__ == '__main__':
    app.run(port=105)