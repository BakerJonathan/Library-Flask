from flask import Blueprint, request, jsonify
from library_app.helpers import token_required
from library_app.models import db, User, Book, book_schema, books_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/books',methods=['POST'])
@token_required
def create_book(current_user_token):
    book_title=request.json['book_title']
    ISBN=request.json['ISBN']
    author=request.json['author']
    publisher=request.json['publisher']
    book_length=request.json['book_length']
    cover_type=request.json['cover_type']
    rental_status=request.json['rental_status']
    renter=request.json['renter']
    language=request.json['language']
    user_token=current_user_token.token

    print(f'BIG TESTER {current_user_token}')

    book=Book(book_title, ISBN, author, publisher, book_length, cover_type, rental_status,renter, language, user_token=user_token)

    db.session.add(book)
    db.session.commit()

    response=book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods=['GET'])
@token_required
def get_books(current_user_token):
    books=Book.query.filter_by(user_token=current_user_token.token).all()
    response=books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>',methods=["GET"])
@token_required
def get_single_car(current_user_token,id):
    book=Book.query.get(id)
    response=book_schema.dump(book)
    return jsonify(response)


@api.route('/books/<id>', methods= ['POST','PUT'])
@token_required
def update_book(current_user_token,id):
    book=Book.query.get(id)
    book.book_title=request.json['book_title']
    book.ISBN=request.json['ISBN']
    book.author=request.json['author']
    book.publisher=request.json['publisher']
    book.book_length=request.json['book_length']
    book.cover_type=request.json['cover_type']
    book.rental_status=request.json['rental_status']
    book.renter=request.json['renter']
    book.language=request.json['language']
    book.user_token=current_user_token.token

    db.session.commit()
    response=book_schema.dump(book)
    return jsonify(response)


@api.route('/books/<id>', methods=['DELETE'])
@token_required
def delete_car(current_user_token,id):
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response=book_schema.dump(book)
    return jsonify(response)