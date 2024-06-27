# Social Media API

This is a FastAPI-based social media API that uses PostgreSQL and SQLAlchemy.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Git

### Installation

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/mbu-peter/fast-api-social-app.git]
    cd fast-api-social-app
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install the requirements:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file in the project root and add your configuration:**

    ```env
    DATABASE_URI=your_postgresql_database_uri
    SECRET_KEY=your_secret_key
    ```

### How to Run

1. **Run the FastAPI server using Uvicorn:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The `--reload` option will automatically restart the server after code changes, which is useful during development.

### API Documentation

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Demo

You can view a live demo of the API at: [https://fast-api-social-app.onrender.com](https://fast-api-social-app.onrender.com)
---

