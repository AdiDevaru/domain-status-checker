# Link Scrapper Django

This web crawler was built using Django, MySQL, and MongoDB, with task management handled by Celery and Redis.

## Features

- Scrapes web data and stores it in MySQL and MongoDB.
- Asynchronous task management using Celery and Redis.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Django
- MySQL
- MongoDB
- Redis
- Celery

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2. **Install dependencies:**

    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**

    Configure your MySQL database in `.env`:

    ```python
    DB_NAME=<your_db_name>
    DB_USER=<your_db_user>
    DB_PASSWORD=<your_db_password>
    DB_HOST=127.0.0.1
    DB_PORT=3306
    ```

4. **Set up the MongoDB connection:**

    Configure your MongoDB connection in `.env`:

    ```python
    MONGO_URI=<your_mongo_connection_string>
    MONGO_DB_NAME=<your_mongo_db_name>
    ```

5. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

## Usage

1. **Start the Redis server:**

    ```bash
    redis-server
    ```

2. **Start the Celery worker:**

    ```bash
    celery -A <your_project_name> worker --loglevel=info --pool=eventlet
    ```

3. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

4. **Start scraping:**

    After starting all the necessary services (Redis, Celery, Django), you can begin scraping by accessing the following endpoint: /socket-index/
   
