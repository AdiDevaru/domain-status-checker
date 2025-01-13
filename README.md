# Link Scrapper Django

This web crawler was built using Django, MySQL, and MongoDB, with task management handled by Celery and Redis.

## Features

- Scrapes web data and stores it in MySQL and MongoDB.
- Asynchronous task management using Celery and Redis.

## Prerequisites

Before running the project, ensure you have the following installed:

* Python ([https://www.python.org/](https://www.google.com/url?sa=E&source=gmail&q=https://www.python.org/))
* Django ([https://www.djangoproject.com/](https://www.google.com/url?sa=E&source=gmail&q=https://www.djangoproject.com/))
* MySQL ([https://www.mysql.com/](https://www.google.com/url?sa=E&source=gmail&q=https://www.mysql.com/))
* MongoDB ([https://www.mongodb.com/](https://www.google.com/url?sa=E&source=gmail&q=https://www.mongodb.com/))
* Redis ([https://redis.io/](https://www.google.com/url?sa=E&source=gmail&q=https://redis.io/))
* Celery ([https://docs.celeryproject.org/](https://www.google.com/url?sa=E&source=gmail&q=https://docs.celeryproject.org/))
* Channels ([https://channels.readthedocs.io/en/stable/](https://channels.readthedocs.io/en/stable/)) 
* Python libraries defined in `requirements.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    ```
    
2. **Create a virtual environment and activate it:**
    
    ```bash
    python3 -m venv <myenvpath>
    ```

    ```bash
    <myenvpath>\Scripts\Activate
    ```

4. **Install the required libraries:**

    Go inside main directory
    
    ```bash
    cd <your-repo>
    ```
    
    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file in the project root directory and add the following environment variables:**

    Configure your MySQL database in `.env`:
    ```python
    DATABASE_NAME (MySQL database name)
    DATABASE_USER (MySQL database username)
    DATABASE_PASSWORD (MySQL database password)
    MONGODB_CONNECTION_STRING (MongoDB connection string)
    MONGODB_DATABASE_NAME (MongoDB database name)
    MONGODB_COLLECTION_NAME (MongoDB collection name)
    ```

6. **Run database migrations:**
    
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
   
