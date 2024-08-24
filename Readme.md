# Cyberpunk Inventory Management System

## Overview

This project is a Cyberpunk-themed inventory management system built with FastAPI, SQLAlchemy, and PostgreSQL. The system allows users to manage in-game items such as cybernetic enhancements, weapons, and gadgets. It supports full CRUD (Create, Read, Update, Delete) operations and is fully Dockerized for easy setup and deployment.


## <ins> Setup Instructions
## Option 1 (Using Docker)

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


### 6. Stop the container
```bash
docker-compose down
```

## Option 2 (Locally Without Docker)

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Anton0729/Cyberpunk-Inventory-Management-System.git
```

### 2. Install Dependencies
Navigate to the project directory
```bash
cd Cyberpunk-Inventory-Management-System
```

Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required Python packages
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the FastAPI application using uvicorn:
```bash
uvicorn app.main:app --reload --port 8001
```


### To run tests use:
```bash
pytest
```