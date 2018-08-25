from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

bookDb = SQLAlchemy(app)


class Book(bookDb.Model):
    __tablename__ = 'books'
    id = bookDb.Column(bookDb.Integer, primary_key=True)
    name = bookDb.Column(bookDb.String(80), nullable=False)
    price = bookDb.Column(bookDb.Float, nullable=False)
    isbn = bookDb.Column(bookDb.Integer)

    def json(self):
        return {'name': self.name, 'price': self.price, 'isbn': self.isbn}

    def add_book(_name, _price, _isbn):
        new_book = Book(name=_name, price=_price, isbn=_isbn)
        bookDb.session.add(new_book)
        bookDb.session.commit()

    def get_all_books():
        return [Book.json(book) for book in Book.query.all()]

    def get_book(_isbn):
        return Book.json(Book.query.filter_by(isbn=_isbn).first())

    def delete_book(_isbn):
        is_successful = Book.query.filter_by(isbn=_isbn).delete()
        bookDb.session.commit()
        return bool(is_successful)

    def update_book_price(_isbn, _price):
        book_to_update = Book.query.filter_by(isbn=_isbn).first()
        book_to_update.price = _price
        bookDb.session.commit()

    def update_book_name(_isbn, _name):
        book_to_update = Book.query.filter_by(isbn=_isbn).first()
        book_to_update.name = _name
        bookDb.session.commit()

    def replace_book(_isbn, _name, _price):
        book_to_replace = Book.query.filter_by(isbn=_isbn).first()
        book_to_replace.price = _price
        book_to_replace.name = _name
        bookDb.session.commit()

    def __repr__(self):
        book_object = {
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn
        }
        return json.dumps(book_object)
