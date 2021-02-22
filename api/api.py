import flask
from flask import request, jsonify
import mysql.connector
import jwt
import json
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="probaaaa"
)
import os

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'RandomString'
app.config["DEBUG"] = True

@app.route('/api/v1/get/users', methods=['GET'])
def getUsers():
    try:
        user = mydb.cursor()
        user.execute("SELECT * FROM user")
        allUsers = user.fetchall()

        json_data_list = []
        for i in allUsers:
            json_data_list.append({"userId":str(i[0]) , "name": i[1] , "email":i[2], "password": str(i[3]), "message":"true"})
        
        return json.dumps(json_data_list)
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

@app.route('/api/v1/create/user', methods=['POST'])
def createUser():
    try:
        user = mydb.cursor()
        user.execute('''INSERT INTO user(name, email, password) VALUES (%s, %s,%s)''', (request.args.get('name'), request.args.get('email'), request.args.get('password')))
        mydb.commit()
        return '{"message":"true"}'
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

@app.route('/api/v1/get/one/user', methods=['GET'])
def gechecktUsers():
    try:
        user = mydb.cursor()
        user.execute('''SELECT * FROM user WHERE password = %s and email = %s''', (request.args.get('password'),request.args.get('email')))
        oneUser = user.fetchone()
        if oneUser == None:
            return '{"message":"none"}'
        return {"userId": str(oneUser[0]) , "name": oneUser[1] , "email": oneUser[2], "password": oneUser[3], "message" : "true"}
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

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
                json_data_list = []
                
                for i in allBooks:
                    json_data_list.append({"bookId" : str(i[0]) , "name" : i[1] , "description" : i[2], "userId" : str(i[3]), "message" : "true"})

                return json.dumps(json_data_list)
            else:
                return '{"message":"false"}'
        else:
            return '{"message":"false"}'
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

@app.route('/api/v1/get/one/book/<id>', methods=['GET'])
def getOneBook(id):
    try:
        if 'x-access-tokens' in request.headers:
            headers = request.headers.get('x-access-tokens')
            decodeToken = jwt.decode(headers , app.config['SECRET_KEY'])
            
            if decodeToken['mod'] == 'normal':
                book = mydb.cursor()
                book.execute('''SELECT * FROM book WHERE bookId = %s''', (id,))
                oneBook = book.fetchone()
                return {"bookId":str(oneBook[0]) , "name":oneBook[1] , "description":oneBook[2], "userId":str(oneBook[3]), "message":"true"}
            else:
                return '{"message":"false"}'
        else:
            return '{"message":"false"}'
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
                return '{"message":"true"}'
            else:
                return '{"message":"false"}'
        else:
            return '{"message":"false"}'
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

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
                return '{"message":"true"}'
            return '{"message":"false"}'
        else:
            return '{"message":"false"}'
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

@app.route('/api/v1/edit/book/<id>', methods=['PUT'])
def editBook(id):
    try:
        book = mydb.cursor()
        book.execute('''UPDATE book SET name = %s, description = %s WHERE bookId = %s''', (request.args.get('name'),request.args.get('description'), id))
        mydb.commit()
        return '{"message":"true"}'
    except mysql.connector.Error as error:
        print(error)
        return '{"message":"false"}'

if __name__ == '__main__':
    app.run(port=105)