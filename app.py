from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

#Load env variables
load_dotenv()

#initiate Flask app
app = Flask(__name__)
CORS(app)

#html render
@app.route('/')
def home():
    return render_template("index.html")

#connect MongoDb to our code
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
books_collection = db["books"]

#GET all books
@app.route('/api/books', methods=["GET"])
def get_books():
    books = []
    for book in books_collection.find():
        book["_id"] = str(book["_id"])
        books.append(book)
    return jsonify(books)

#Add books 
@app.route('/api/books', methods=["POST"])
def add_books():
    book = request.get_json()
    books_collection.insert_one(book)
    return jsonify ({"Message": "Book added successfully"}), 201

#Delete book
@app.route('/api/books/<id>', methods=["DELETE"])
def delete_books(id):
    books_collection.delete_one({"_id": ObjectId(id)})
    return jsonify ({"Message": "Book deleted successfully"}), 200

#search books by title or author
@app.route('/api/books/search', methods=["GET"])
def search_books():
    query = request.args.get("query", "")  
    if not query:
        return jsonify({"error": "Please provide a search query"}), 400

    results = books_collection.find({
        "$or": [
            {"title":  {"$regex": query, "$options": "i"}},  
        ]
    })

    books = []
    for book in results:
        book["_id"] = str(book["_id"])
        books.append(book)

    return jsonify(books), 200

if __name__ == "__main__":
    app.run(debug=True)


        






