# Cyberpunk Inventory Management System

## Overview

This project is a Cyberpunk-themed inventory management system built with FastAPI, SQLAlchemy, and PostgreSQL. The system allows users to manage in-game items such as cybernetic enhancements, weapons, and gadgets. It supports full CRUD (Create, Read, Update, Delete) operations and is fully Dockerized for easy setup and deployment.

API Documentation
https://docs.google.com/document/d/1mFH4yAI1E3IzMou-yT8c5PPu1uHhQ_gV/edit?usp=sharing&ouid=110472722426617783568&rtpof=true&sd=true
[link](doc:[linking-to-pages#anchor-links](https://docs.google.com/document/d/1mFH4yAI1E3IzMou-yT8c5PPu1uHhQ_gV/edit?usp=sharing&ouid=110472722426617783568&rtpof=true&sd=true))


## Features
1. FastAPI with Postgres setup
2. Docker container with docker-compose
3. JWT User Authentication
4. Writing Pytest with Coverage
5. Manage Migrations with Alembic script

## <ins> Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Anton0729/Cyberpunk-Inventory-Management-System.git
```

### 2. Run Docker Desktop

### 3. Build the container
```bash
docker-compose build
```

### 4. Run the container
```bash
docker-compose up
```

### 5. Access the Application

- Application: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc


### 6. Delete the container
```bash
docker-compose down
```
<br>

### Running Tests:
To run tests for this project, follow these steps:
### 1. Ensure the test database is created
You need to create a test database before running the tests. You can do this using the following command:
```bash
docker-compose exec db psql -U postgres -c "CREATE DATABASE test_db_cyberpunk_inventory;"
```

### 2. Run the tests
Once the test database is set up, you can run the tests using the following command:
```bash
docker-compose run --rm web sh -c "pytest"
```

### 3. Test Coverage:
To check the test coverage, follow these steps:
```bash
docker-compose run --rm web sh -c "coverage run -m pytest && coverage report"
```
