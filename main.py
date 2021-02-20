from flask import Flask, jsonify, render_template, redirect, url_for, request, session
import datetime	
import hashlib
import requests
import json
import re
import jwt
from validate_email import validate_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RandomString'

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        
        return render_template('register.html')
    else:
        errors = []
        req = requests.get('http://localhost:105/api/v1/get/users')
        users = json.loads(req.content)
        for i in users:
            if(request.form['email'] == i[2]):
                return render_template('register.html', userExist = 'User already exist, please login')
        
        if(validate_email(request.form['email']) == False):
            errors.append("Invalid email address")
        if(len(request.form['password']) <= 6):
            errors.append("Password must have more than 6 caracters")
        if(bool(re.search(r'\d', request.form['password'])) == False):
            errors.append("Password must contain at least one number")
        if(bool(re.search('^[a-zA-Z0-9]*$',request.form['name']))==False):
            errors.append("Name must not have special caracters")
        if(request.form['name'][0].isdigit()):
            errors.append("Name must not start with number")
        if(len(errors) != 0 ):
            return render_template('register.html', errors = errors)

        hash_object = hashlib.sha256(request.form['password'].encode())
        password_hashed = hash_object.hexdigest()
        params = {
            'name' : request.form['name'], 
            'email' : request.form['email'],
            'password' : password_hashed
        }
        requests.post('http://localhost:105/api/v1/create/user', params = params)
        return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        hash_object = hashlib.sha256(request.form['password'].encode())
        password_hashed = hash_object.hexdigest()
        params = {
            'password' : password_hashed,
            'email' : request.form['email']
        }
        req = requests.get('http://localhost:105/api/v1/get/one/user', params = params)
        user = json.loads(req.content)
        if len(user) == 0:
            return 'Wrong login info!'
        session['_id'] = str(user[0])
        
        return render_template('user_home.html', id = session['_id'])

@app.route('/books', methods = ['GET'])
def books():
    if '_id' not in session:
        return 'You are not logged in!'

    if 'token' in session:
        headers = {'x-access-tokens': session['token']}
    else:
        headers = {'no-token': '0'}
    req = requests.get('http://localhost:105/api/v1/get/book/' + session['_id'], headers = headers)
    books = json.loads(req.content)
    
    if books == False:
        return jsonify({"message": "ERROR: Unauthorized"}), 401 
    return render_template('books.html' , books = books)

@app.route('/create_book', methods = ['GET', 'POST'])
def create_book():
    if request.method == 'GET':
        return render_template('create_book.html')  
    params = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'userId' : session['_id']
    }  
    if 'token' in session:
        headers = {'x-access-tokens': session['token']}
    else:
        headers = {'no-token': '0'}
    
    req = requests.post('http://localhost:105/api/v1/create/book', params = params, headers = headers)
    check = json.loads(req.content)
    
    if check == False:
        return jsonify({"message": "ERROR: Unauthorized"}), 401 
    return redirect(url_for('books'))

@app.route('/delete/<id>', methods = ['GET'])
def delete(id):
    if 'token' in session:
        headers = {'x-access-tokens': session['token']}
    else:
        headers = {'no-token': '0'}
    req = requests.delete('http://localhost:105/api/v1/delete/book/' + id, headers = headers)
    check = json.loads(req.content)
    if check == False:
        return jsonify({"message": "ERROR: Unauthorized"}), 401 
    return redirect(url_for('books'))

@app.route('/edit_book/<id>', methods = ['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        if 'token' in session:
            headers = {'x-access-tokens': session['token']}
        else:
            headers = {'no-token': '0'}
        req = requests.get('http://localhost:105/api/v1/get/one/book/' + id, headers = headers)
        book = json.loads(req.content)
        
        if book == False:
            return jsonify({"message": "ERROR: Unauthorized"}), 401 
        
        return render_template('edit_book.html', book = book)
    params = {
        'id' : id,
        'name' : request.form['name'],
        'description' : request.form['description']
    }  
    
    requests.put('http://localhost:105/api/v1/edit/book', params = params)
    return redirect(url_for('books'))

@app.route('/create_token')
def create_token():
    
    token = jwt.encode({"mod" : "normal", "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])
    session['token'] = token
    return redirect(url_for('books'))

@app.route('/read_only_token')
def read_only_token():
    
    token = jwt.encode({"mod" : "readonly", "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])
    session['token'] = token
    return redirect(url_for('books'))

if __name__ == '__main__':
	app.run()