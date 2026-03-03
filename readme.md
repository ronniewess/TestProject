# Task Manager API
A RESTful Task Manager API built with: 
- Django 4.2
- Django REST Framework
- PostgreSQL
- Uvicorn (Fast API)

This project uses a Python virtual environment (venv) for isolating all the dependencies requried.
After installation and setup, you will be able to create, get, update, and delete tasks. 

## Project Setup
### Clone the respository 
``` 
git clone https://github.com/ronniewess/TestProject.git
cd TestProject
```

### Create the Python VM
```
python -m venv venv
```

### Activate it - Mac/Linux
```
source venv/bin/activate
```

### Or...Activate it - Windows
```
venv\Scripts\activate
```

### Install All Dependencies
```
pip install -r requirements.txt
```

## PostgreSQL  Database Setup
### Open PostgreSQL
```
psql -U postgres
```
### Create Database
```
CREATE DATABASE task_api_db
```
### Create Database User
```
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE task_api_db TO your_db_user;
```
Then exit: 
```
\q
```
## Enviornmental Setup
### Create .env File
```
cp .env.example .env
```
### Match .env setup
```
DEBUG=True
SECRET_KEY=your_generated_secret_key

DB_NAME=task_api_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
## Database Migrations
Run needed database migrations: 
```
python manage.py migrate
```

## Run Application with Fast API
```
uvicorn main:app --reload
```
Open a web browser and enter the appropriate URL to access the web UI.
Note: The default port is 8000. The following command will adjust to set a custom port.
```
uvicorn fastapi_app:app --reload --port 8001
```
In this case, the web URL is http://127.0.0.1:8001/docs#/.

From here, you should be able to test each endpoint with appropriate data.
