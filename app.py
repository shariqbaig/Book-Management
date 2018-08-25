from flask import jsonify, request, Response, json
from BookModel import Book
from UserModel import User
from settings import app
import jwt
import datetime
import sys
from functools import wraps

# books = Book.get_all_books()
DEFAULT_PAGE_LIMIT = 3


def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn"
            in bookObject):
        return True
    else:
        return False


def validUserObject(userObject):
    if ("username" in userObject and "password" in userObject):
        return True
    else:
        return False


def valid_put_request_data(bookObject):
    if ("name" in bookObject and "price" in bookObject):
        return True
    else:
        return False


def valid_patch_request_data(bookObject):
    if ("name" in bookObject or "price" in bookObject):
        return True
    else:
        return False


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper


@app.route('/books/page/<int:page_number>')
def get_paginated_books(page_number):
    books = Book.get_all_books()
    LIMIT = request.args.get('limit', DEFAULT_PAGE_LIMIT, int)
    startIndex = (page_number - 1) * LIMIT
    endIndex = len(books)

    if(LIMIT < endIndex):
        endIndex = LIMIT * page_number
        if(endIndex > len(books)):
            endIndex = len(books)

    print(startIndex)
    print(endIndex)
    return jsonify({'books': books[startIndex:endIndex]})


@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])

    match = User.username_password_match(username, password)

    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=360000)
        print(expiration_date)
        token = jwt.encode({'exp': expiration_date},
                           app.config['SECRET_KEY'], algorithm='HS256')
        return token

    else:
        Response('', status=401, mimetype='application/json')


@app.route('/create', methods=['POST'])
def create_user():
    request_data = request.get_json()
    if(validUserObject(request_data)):
        User.createUser(request_data['username'], request_data['password'])
        response = Response("", status=201, mimetype='application/json')
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid User Object passed in request",
            "helpString": "Data passed in similar to this {'username': 'user', 'password': 'pass' }"
        }

        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response


@app.route('/books')
def get_books():
    return jsonify({'books': Book.get_all_books()})


@app.route('/')
def home():
    return '<h1>Book Management System</h1>'


@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)


@app.route('/books', methods=['POST'])
@token_required
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        try:
            Book.add_book(request_data['name'],
                          request_data['price'], request_data['isbn'])
        except:
            print('Unexpected error: ', sys.exc_info()[0])
            print('more error', sys.exc_info()[1])

        response = Response("", status=201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(request_data['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price': 7.99, 'isbn': 792321354533 }"
        }

        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response


@app.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def replace_book(isbn):
    request_data = request.get_json()
    if(not valid_put_request_data(request_data)):
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price': 7.99 }"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response

    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response("", status=204, mimetype='application/json')
    return response


@app.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def update_book(isbn):
    request_data = request.get_json()
    if(not valid_patch_request_data(request_data)):
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price': 7.99 }"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response

    if("name" in request_data):
        Book.update_book_name(isbn, request_data['name'])
    if("price" in request_data):
        Book.update_book_price(isbn, request_data['price'])

    response = Response("", status=204, mimetype='application/json')
    response.headers['Location'] = "/books/" + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):
    if (Book.delete_book(isbn)):
        response = Response("", status=204, mimetype='application/json')
    return response

    invalidBookObjectErrorMsg = {
        "error": "Book with the ISBN number that was provided was not found, so therefore unable to delete."
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg),
                        status=404, mimetype='application/json')
    return response


# app.run(port=5000)
