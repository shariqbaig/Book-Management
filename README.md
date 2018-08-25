# Book-Management

REST APIs using FLASK Microframework

Heroku Link: https://gentle-woodland-25892.herokuapp.com/

Available Routes are:

1. GET **-->** / **-->** Home
2. GET **-->** /books **-->** To get all books
3. GET **-->** /books/12345678 **-->** To get book by ISBN
4. GET **-->** /books/page/1?limit=100 **-->** To get books page and limit vise

5. POST **-->** /login **-->** To login and get an access token (JWT)
   For Example: { "username": "test", "password": "pass" } (Content-Type: application/json)

6. POST **-->** /create **-->** To create new user in database
   For Example: { "username": "test", "password": "pass" } (Content-Type: application/json)

7. POST **-->** /books?token=**token-here** **-->** To post a book in database
   For Example: { "name": "ABC Book", "price": 6.99, "isbn": 12345678 } (Content-Type: application/json)

8. PUT --> /books/12345678?token=**token-here** **-->** To replace a book in database
   For Example: { "name": "ABC Book", "price": 6.99 } (Content-Type: application/json)

9. PATCH **-->** /books/12345678?token=**token-here** **-->** To update either price or name or both of books in database
   For Example: { "name": "ABC Book" } { "price": 6.99 } (Content-Type: application/json)

10. DELETE **-->** /books/12345678?token=**token-here** **-->** To delete a book in database
