To design and implement the mock APIs as specified, we will follow these steps:
1. API Design and Implementation
API Endpoints and JSON Schemas
1. User Registration: POST /users/register
- Request:
    {
        "username": "string",
        "password": "string",	
        "email": "string"
    }
- Response:
    - Success:
        {
            "userId": "string",
            "message": "User registered successfully"
        }
    - Error:
        {
            "error": "User already exists"
        }

2. User Login: POST /users/login
- Request:
    {
        "username": "string",
        "password": "string"
    }
-Response:
    - Success:
        {
            "token": "string",
            "message": "Login successful"
        }
    - Error:
        {
            "error": "Invalid username or password"
        }

3. Search Books: GET /books?search=query
- Request: (Query Parameter)
    /books?search=string
- Response:
    - Success:
        {
            "books": [
                {
                    "bookId": "string",
                    "title": "string",
                    "author": "string",
                    "description": "string",
                    "price": "number"
                }
            ]
        }
    - Error:
        {
            "error": "No books found"
        }

4. Add to Cart: POST /users/{userId}/cart**
-Request:
    {
        "bookId": "string",
        "quantity": "number"
    }
- Response:
    - Success:
        {
            "cartId": "string",
            "message": "Book added to cart"
        }
    - Error:
        {
            "error": "Book not found"
        }

5. Checkout: POST /users/{userId}/checkout**
- Request:
    {
        "paymentMethod": "string",
        "address": "string"
    }
- Response:
    - Success:
        {
            "orderId": "string",
            "message": "Checkout successful"
        }
    - Error:
        {
            "error": "Payment declined"
        }
        
