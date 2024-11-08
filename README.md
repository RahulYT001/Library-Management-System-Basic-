Book Management API

This project is a RESTful API built using Flask to manage a collection of books. It allows you to search, add, update, delete, and view books in the system.

Features

Search Books by name, author, or ISBN.
View All Books or a specific book by its ID.
Add New Books with essential details like name, author, price, and ISBN.
Update Existing Books by providing new data for a specific book.
Delete Books from the collection.

Technologies Used

Flask (Python Web Framework)
JSON (for data exchange)
REST API
API Endpoints

1. Get All Books
Endpoint: /api/books
Method: GET
Description: Returns a list of all books in the collection.
Response:
json
Copy code
{
  "books": [...]
}

2. Get Book by ID
Endpoint: /api/books/<int:bookid>
Method: GET
Description: Returns the details of a book by its ID.
Response:
json
Copy code
{
  "id": 1,
  "Name": "Book Name",
  "author": "Author Name",
  ...
}

3. Search for Books
Endpoint: /api/books/search?q=<query>
Method: GET
Description: Search books by name, author, or ISBN.
Response (Example):
json
Copy code
{
  "books": [
    {
      "id": 1,
      "Name": "Book Name",
      "author": "Author Name",
      ...
    }
  ]
}

4. Add a New Book
Endpoint: /api/books
Method: POST
Request Body:
json
Copy code
{
  "Name": "New Book",
  "author": "Author Name",
  "price": 300,
  "ISBN": 123456789
}
Response:
json
Copy code
{
  "id": 16,
  "Name": "New Book",
  ...
}

5. Update a Book
Endpoint: /api/books/update/<int:bookid>
Method: PUT
Description: Update the details of an existing book by its ID.
Request Body (Example):
json
Copy code
{
  "price": 350
}

6. Delete a Book
Endpoint: /api/books/remove/<int:bookid>
Method: DELETE
Description: Delete a book from the collection by its ID.
Response:
json
Copy code
{
  "Result": "Book deleted"
}
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/book-management-api.git
cd book-management-api
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
The API will run on http://127.0.0.1:5000/.

Usage
Use tools like Postman or curl to interact with the API.
You can also build a frontend to interact with the API and serve it using Flask.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests to enhance the project.