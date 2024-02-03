# Attendance System

Automated attendance system backend built with Django.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up the Database](#setting-up-the-database)
  - [Running the Development Server](#running-the-development-server)
- [Folder Structure](#folder-structure)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Scripts](#scripts)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python (version x.x.x)
- Pipenv
- SQLite or another database of your choice

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/attendance-system.git
   ```

2. Change into the project directory:

   ```bash
   cd attendance-system
   ```

3. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

### Setting Up the Database

Run the initial migrations to set up the database:

```bash
pipenv run python manage.py migrate
```

### Running the Development Server

Activate the virtual environment:

```bash
pipenv shell
```

Run the development server:

```bash
pipenv run python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Folder Structure

The project follows a standard Django project structure:

```
attendance_system/
|-- attendance_system/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings/
|   |   |-- __init__.py
|   |   |-- base.py
|   |   |-- local.py
|   |   |-- production.py
|   |-- urls.py
|   |-- wsgi.py
|-- apps/
|   |-- accounts/
|   |   |-- migrations/
|   |   |-- templates/
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- attendance/
|   |   |-- migrations/
|   |   |-- templates/
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|-- static/
|-- templates/
|-- media/
|-- db.sqlite3
|-- manage.py
|-- Pipfile
|-- Pipfile.lock
|-- .gitignore
|-- .env
|-- README.md
|-- requirements.txt
|-- scripts/
|   |-- setup_database.sh
|   |-- run_tests.sh
|   |-- create_superuser.sh
|-- Dockerfile
|-- docker-compose.yml
|-- .dockerignore
```

## Environment Variables

The project uses environment variables for configuration. Create a `.env` file in the project root and define the following variables:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
```

## API Documentation

The API documentation is available at [API Documentation](./docs/api.md).

## Scripts

Helpful scripts are available in the `scripts/` directory. Run them using:

```bash
pipenv run sh scripts/script_name.sh
```

- `setup_database.sh`: Sets up the database.
- `run_tests.sh`: Runs tests.
- `create_superuser.sh`: Creates a superuser.

## Docker

... (Include information on Docker setup and usage if applicable)

## Contributing

We welcome contributions! Read the [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).