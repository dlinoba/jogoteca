# Jogoteca – Game Catalog Management System

A web application built with **Python, Flask, and MySQL** to manage a game catalog, including user authentication and administration features.

Originally developed as part of an Alura learning project, this application was extended with additional features such as user registration, password management, dynamic game search, and Docker containerization.

## Features

### Game Management
- Register new games with name, category, and console information.
- Edit existing game records.
- Delete games from the catalog.
- List registered games.
- Search games dynamically by name.

### User Management
- User authentication and session management.
- Register new users.
- Change the password of the authenticated user.
- Password hashing using Flask-Bcrypt.
- Access control for protected application pages.

### Application Security
- CSRF protection using Flask-WTF.
- Form validation with WTForms.
- Password hashing and verification.
- Session-based authentication.

### Containerization
- Dockerfile configuration for the application and database.
- Docker Compose configuration to orchestrate the services.
- MySQL database initialization through an SQL script.

## Technologies

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend development |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration and ORM |
| MySQL 5.7 | Relational database |
| Flask-Bcrypt | Password hashing |
| Flask-WTF / WTForms | Form validation and CSRF protection |
| HTML / CSS / JavaScript | Frontend development |
| Bootstrap | User interface styling |
| Docker | Application containerization |
| Docker Compose | Container orchestration |

## Application Architecture

The application follows a modular structure, separating the main Flask configuration, database models, game routes, user routes, and form definitions.

```text
jogoteca/
│
├── Dockerfile
├── docker-compose.yml
├── config.py
├── jogoteca.py
├── models.py
├── views_jogos.py
├── views_user.py
├── helpers.py
├── prepara_banco.sql
├── requirements.txt
│
├── static/
│   ├── app.css
│   ├── app.js
│   └── ...
│
└── templates/
    ├── template.html
    ├── login.html
    ├── lista.html
    ├── novo.html
    ├── editar.html
    ├── novousuario.html
    ├── alterarsenha.html
    └── search_results.html
```

## Database

The application uses MySQL as its relational database and Flask-SQLAlchemy to map application entities to database tables.

The main entities are:

### Games (`jogos`)

Stores the game catalog.

| Column | Description |
|---|---|
| id | Primary key |
| nome | Game name |
| categoria | Game category |
| console | Gaming platform |

### Users (`usuarios`)

Stores application user accounts.

| Column | Description |
|---|---|
| nickname | User identifier and primary key |
| nome | User name |
| senha | Hashed password |

The `prepara_banco.sql` script creates the database, creates the main tables, and inserts initial sample records.

## Getting Started

### Prerequisites

To run the application locally, you need:

- Python 3.11
- MySQL
- Docker and Docker Compose (for containerized execution)

### Install Dependencies

Clone the repository:

```bash
git clone https://github.com/dlinoba/jogoteca.git
cd jogoteca
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Database Configuration

Review `config.py` and configure the SQLAlchemy connection string according to your MySQL environment.

Execute the SQL script to create the database and its initial records:

```sql
SOURCE prepara_banco.sql;
```

### Run the Application

Start the Flask application:

```bash
python jogoteca.py
```

Open your browser:

```text
http://localhost:8000
```

## Docker

The repository includes a `Dockerfile` and a `docker-compose.yml` intended to containerize the application and MySQL database.

The container configuration is provided as part of the project to demonstrate application packaging and service orchestration.

**Note:** Review the current Docker configuration before running it. The application and database connection settings, Docker build stages, and Compose service definitions require alignment for a reproducible containerized deployment.

## Project Purpose

This project demonstrates practical experience with:

- Python backend development.
- Flask application structure and routing.
- Relational database integration with MySQL.
- Object-relational mapping using SQLAlchemy.
- User authentication and password management.
- Form validation and CSRF protection.
- CRUD operations.
- Dynamic database queries.
- Docker-based application packaging.

It represents a practical learning project focused on web application development, database integration, and containerization.

## Author

**Deyvid Linoba**

- GitHub: [github.com/dlinoba](https://github.com/dlinoba)
- LinkedIn: [linkedin.com/in/deyvid-linoba](https://www.linkedin.com/in/deyvid-linoba/)
