from functions.api_functions import *

def test_register_user_success():                   #User Registration is successful
    response = register_user(payload_user_register("new_user","password123","user@gmail.com"))
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_register_user_already_exists():        #User Registration for user that already exist
    response = register_user(payload_user_register("existing_user","password123","existing@gmail.com"))
    assert response.status_code == 404
    assert response.json()["detail"] == "User already exists"

def test_register_username_missing():       #Username missing during user registration
    response = register_user(payload_blank_username())
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert (detail[0]["msg"]) == "Field required"

def test_non_existent_endpoint():       #Non-existent URL
    response = register_user_notfound(payload_user_register("new_user","password123","user@gmail.com"))
    assert response.status_code == 404

def test_login_user_success():          #User Login success
    response = login_user(payload_login("valid_user","valid_password"))
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_login_user_invalid_credentials():      #User attempts to login with invalid crdentials
    response = login_user(payload_login("invalid_user","invalid_password"))
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"

def test_search_books_success():            #User able to search book successfully
    response = search_books("Sample Book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) > 0
    assert books[0]["title"] == "Sample Book"

def test_search_books_not_found():      #User not able to search book
    response = search_books("unknown")
    assert response.status_code == 404
    assert response.json()["detail"] == "No books found"

def test_add_to_cart_success():     #Book successfully added to cart
    response = add_to_cart(payload_add_cart("book-123",1))
    assert response.status_code == 200
    assert response.json()["message"] == "Book added to cart"

def test_add_to_cart_book_not_found():          #Trying to add unknown book to the cart
    response = add_to_cart(payload_add_cart("invalid-book",1))
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

def test_checkout_success():        #successful checkout
    response = checkout(payload_checkout("valid_method","123 street"))
    assert response.status_code == 200
    assert response.json()["message"] == "Checkout successful"

def test_checkout_payment_declined():       #Failed checkout
    response = checkout(payload_checkout("invalid_method","123 street"))
    assert response.status_code == 402
    assert response.json()["detail"] == "Payment declined"
