# API Testing Project

This project demonstrates the design and implementation of mock APIs and automated testing using FastAPI, pytest, and Postman.

## Test Coverage
User Registration:
- Successfully registers a new user.
- Attempts to register with an already existing username.
- Attempts to register without providing a username.

Error Handling:
Handles "URL not found" errors.

User Login:
- Successfully logs in with valid credentials.
- Fails to log in due to invalid credentials.

Book Search:
- Successfully searches for an available book.
- Attempts to search for a book that is not in the catalog.

Shopping Cart:
- Successfully adds a book to the cart.
- Fails to add a book to the cart.

Checkout Process:
- Successfully completes the checkout process.
- Fails to complete the checkout process.

## Setup

### Prerequisites
- Python 3.6+
- Postman

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SayaliYadavGit/api-testing-project.git
    cd api-testing-project
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Start the FastAPI server:
    ```bash
    cd mock-apis/source
    uvicorn mock-apis.source.main:app --reload
    ```

## Running Tests

### Automated Tests with pytest
Run the tests with:
```bash
cd tests/integration 
pytest test_api.py -v
 ```

## Project Structure
```bash
/api-testing-project
  /functions        # Functions used in Tests
  /mock-apis
    /source         # Source code for mock APIs
  /tests
    /integration    # Integration tests
  README.md         # Project documentation
  requirements.txt  # Python dependencies
 ```

## Manual Tests with Postman
- Open Postman.

- Run the requests to manually test the API endpoints.

#### Along with this adding json file for postman Collection in main folder - api-testing-project.json

Test Cases Covered
With this setup, you have a complete solution for mock APIs and automated testing. This project is ready for further development and integration into a CI pipeline.
