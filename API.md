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
    - 400: User already exists

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
    - 401: Invalid username or password

### Search Books
- **Endpoint:** GET /books?search=query
- **Responses:**
    - 200: List of books matching the search query
    - 404: No books found

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
    - 404: Book not found

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
    - 402: Payment declined

