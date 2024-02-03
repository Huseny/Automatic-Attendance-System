# Attendance System

Automated attendance system backend built with Django.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up the Database](#setting-up-the-database)
  - [Running the Development Server](#running-the-development-server)
- [Directory Structure](#directory-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python (version 3.10)
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Huseny/Automatic-Attendance-System.git
   ```

2. Change into the project directory:

   ```bash
   cd Automatic-Attendance-System
   ```

3. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

### Setting Up the Database

Run the initial migrations to set up the database:

```bash
python manage.py migrate
```

### Running the Development Server

Activate the virtual environment:

```bash
pipenv shell
```

Run the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Directory Structure

Please the following folder structure when adding your contribution:

```
Automatic-Attendance-System/
|-- AI Students Picture/
|-- attendance/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   |-- detection/
|   |   |-- __init__.py
|   |   |-- ...
|   |-- recognition/
|   |   |-- __init__.py
|   |   |-- ...
|-- db.sqlite3
|-- manage.py
|-- Pipfile
|-- Pipfile.lock
|-- .gitignore
|-- README.md
|-- LICENSE
```

## Environment Variables

The project uses environment variables for configuration. Create a `.env` file in the project root and define the following variables:

```env
DEBUG=TRUE
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=allowed_hosts
ADMIN_USER=superuser_username
ADMIN_PASSWORD=superuser_password
```

## Contributing

1. pull from main before starting a new feature.
2. Create a new branch for the feature you are working on.
3. Checkout to the new branch and start working on the feature.
4. Make changes to the codebase.
5. Commit changes using the following naming convention: [TYPE-OF-CHANGE](SCOPE): [SHORT-DESCRIPTION].
6. Push changes.
7. Create a pull request to merge the new branch into dev branch.

Use the following template for commit messages:

```
 - chore(folders): renamed/restructured folders
 - feat(feature): implement UI for a feature
 - fix(feature): fix a not working feature
 - style(feature): refined UI for a feature
```


## License

This project is licensed under the [MIT License](LICENSE).