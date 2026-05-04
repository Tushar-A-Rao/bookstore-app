from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

#Load env variables
load_dotenv()

#initiate Flask app
app = Flask(__name__)
CORS(app)

#connect MongoDb to our code
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
books_collection = db["books"]

#search books by title or author
@app.route('/api/books/search', methods=["GET"])
def search_books():
    query = request.args.get("query", "")  
    if not query:
        return jsonify({"error": "Please provide a search query"}), 400

    results = books_collection.find({
        "$or": [
            {"title":  {"$regex": query, "$options": "i"}},  {"author": {"$regex": query, "$options": "i"}}
        ]
        
    })

    books = []
    for book in results:
        book["_id"] = str(book["_id"])
        books.append(book)

    return jsonify(books), 200

if __name__ == "__main__":
    app.run(debug=True, port=5002)