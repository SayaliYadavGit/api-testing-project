# API Testing Project

This project demonstrates the design and implementation of mock APIs and automated testing using FastAPI, pytest, and Postman.

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
    uvicorn mock-apis.source.main:app --reload
    ```

## Running Tests

### Automated Tests with pytest
Run the tests with:
```bash
pytest test_api.py
 ```

## Project Structure
```bash
/api-testing-project
  /functions
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

#####Along with this adding json file for postman Collection in main folder - api-testing-project.json

With this setup, you have a complete solution for mock APIs and automated testing. This project is ready for further development and integration into a CI pipeline.
