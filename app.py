from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# Existing books data
books = [
    {"id": 1, "Name": "12 Rules for Life", "author": "Jordan Peterson", "price": 300, "availability": True, "ISBN": 432343214},
    {"id": 2, "Name": "Atomic Habits", "author": "James Clear", "price": 450, "availability": True, "ISBN": 123456789},
    {"id": 3, "Name": "The Alchemist", "author": "Paulo Coelho", "price": 200, "availability": True, "ISBN": 987654321},
    {"id": 4, "Name": "Sapiens", "author": "Yuval Noah Harari", "price": 500, "availability": False, "ISBN": 654321987},
    {"id": 5, "Name": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "price": 350, "availability": True, "ISBN": 456123789},
    {"id": 6, "Name": "The Power of Now", "author": "Eckhart Tolle", "price": 400, "availability": False, "ISBN": 321654987},
    {"id": 7, "Name": "Educated", "author": "Tara Westover", "price": 320, "availability": True, "ISBN": 789123456},
    {"id": 8, "Name": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "price": 250, "availability": True, "ISBN": 159753468},
    {"id": 9, "Name": "Man's Search for Meaning", "author": "Viktor E. Frankl", "price": 300, "availability": True, "ISBN": 852369741},
    {"id": 10, "Name": "The Four Agreements", "author": "Don Miguel Ruiz", "price": 280, "availability": True, "ISBN": 963258741},
    {"id": 11, "Name": "Becoming", "author": "Michelle Obama", "price": 600, "availability": False, "ISBN": 741852963},
    {"id": 12, "Name": "The Lean Startup", "author": "Eric Ries", "price": 450, "availability": True, "ISBN": 147258369},
    {"id": 13, "Name": "Outliers", "author": "Malcolm Gladwell", "price": 350, "availability": True, "ISBN": 258369147},
    {"id": 14, "Name": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 150, "availability": True, "ISBN": 753159486},
    {"id": 15, "Name": "Dune", "author": "Frank Herbert", "price": 500, "availability": False, "ISBN": 654987123}
]

# Track highest id to prevent duplicates
book_id_counter = max(book['id'] for book in books) + 1

@app.route("/api/books/search", methods = ["GET"])
def search_book():
    query = request.args.get("q", " ").lower()
    if not query:
        return jsonify({"Error: No query provided"}), 400
    results = [b for b in books if query in b["Name"].lower() or 
               query in b["author"].lower() or 
               query in str(b["ISBN"]).lower()]
    if not results:
        return jsonify({"books": [], "message": "No books found."})

    return jsonify({"books": results})


@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify({"books": books})

@app.route("/api/books/<int:bookid>", methods=["GET"])
def get_book_id(bookid):
    book = next((b for b in books if b["id"] == bookid), None)
    if book is None:
        return jsonify({"Error": "Book not found."}), 404
    return jsonify(book)

@app.route("/api/books", methods=["POST"])
def add_book():
    global book_id_counter
    new_book = request.json
    required_fields = ["Name", "author", "price", "ISBN"]
    for field in required_fields:
        if field not in new_book:
            return jsonify({"Error": f"{field} is required"}), 400
    
    # Assign unique ID using the counter
    new_book["id"] = book_id_counter
    new_book["availability"] = True
    books.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route("/api/books/update/<int:bookid>", methods=["PUT"])
def updating_book(bookid):
    updated_data = request.json
    book = next((b for b in books if b["id"] == bookid), None)
    if book is None:
        return jsonify({"Error": "Book not found"}), 404
    
    book.update(updated_data)
    return jsonify(book)

@app.route("/api/books/remove/<int:bookid>", methods=["DELETE"])
def book_delete(bookid):
    global books
    books = [b for b in books if b["id"] != bookid]
    return jsonify({"Result": "Book deleted"}), 200

@app.route('/')
def serve_frontend():
    return send_from_directory('', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
