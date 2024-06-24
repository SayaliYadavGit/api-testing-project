## API Documentation

### User Registration
- **Endpoint:** POST /users/register
- **Request Body:**
    ```json
    {
        "username": "string",
        "password": "string",
        "email": "string"
    }
    ```
- **Responses:**
    - 200: User registered successfully
        ```json
        {
            "message": "User registered successfully",
            "userId": "string"
        }
        ```
    - 404: User already exists
        ```json
         {
            "detail": "User already exists"
         }
        ```
    - 422: Missing Username
        ```json
        {
            {
                "detail": [
                      {
                         "type": "string",
                         "loc": [
                         "body",
                         "username"
                          ],
                                "msg": "Field required",
                                "input": {
                                    "password": "string",
                                    "email": "string"
                                }
                      }
                ]
            }
        }
        ```

### User Login
- **Endpoint:** POST /users/login
- **Request Body:**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
- **Responses:**
    - 200: Login successful
        ```json
        {
            "message": "Login successful",
            "token": "string"
        }
        ```
    - 401: Invalid username or password
        ```json
        {
           "detail": "Invalid username or password"
        }
        ```

### Search Books
- **Endpoint:** GET /books?search=query
- **Responses:**
    - 200: List of books matching the search query
        ```json
        {
            "books": [
                {
                    "id": "string",
                    "title": "string",
                    "author": "string",
                    "summary": "string"
                }
            ]
        }
        ```
    - 404: No books found
        ```json
        {
            "detail": "No books found"
        }
        ```

### Add to Cart
- **Endpoint:** POST /users/{userId}/cart
- **Request Body:**
    ```json
    {
        "bookId": "string",
        "quantity": "number"
    }
    ```
- **Responses:**
    - 200: Book added to cart
        ```json
        {
            "message": "Book added to cart successfully",
            "cartId": "string"
        }
        ```
    - 404: Book not found
        ```json
        {
           "detail": "No books found"
        }
        ```

### Checkout
- **Endpoint:** POST /users/{userId}/checkout
- **Request Body:**
    ```json
    {
        "paymentMethod": "string",
        "address": "string"
    }
    ```
- **Responses:**
    - 200: Checkout successful
        ```json
        {
            "message": "Checkout successful",
            "orderId": "string"
        }
        ```
    - 402: Payment declined
        ```json
        {
           "detail": "Payment declined"
        }
        ```
