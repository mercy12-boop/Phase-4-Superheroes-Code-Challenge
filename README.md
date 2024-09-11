# Superheroes API

A RESTful API built with Flask for managing superheroes, their powers, and the relationship between heroes and their powers.

## Features

- Retrieve a list of heroes and their details
- Retrieve details of a specific hero by ID
- Retrieve a list of powers and their details
- Retrieve details of a specific power by ID
- Update a power's details
- Create a new hero-power relationship
- Validate and handle errors for invalid inputs

## Technologies Used

- Flask
- Flask-RESTful
- Flask-Migrate
- Flask-SQLAlchemy
- SQLite

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

    The application will be available at `http://localhost:5555`.

## API Endpoints

### Heroes

- **GET `/heroes`**: Retrieve a list of all heroes.
- **GET `/heroes/<int:id>`**: Retrieve details of a specific hero by ID.

### Powers

- **GET `/powers`**: Retrieve a list of all powers.
- **GET `/powers/<int:id>`**: Retrieve details of a specific power by ID.
- **PATCH `/powers/<int:id>`**: Update details of a specific power by ID.

### HeroPower

- **POST `/hero_powers`**: Create a new hero-power relationship.

## Error Handling

- **404 Not Found**: Returned if a hero or power with the specified ID does not exist.
- **400 Bad Request**: Returned if the request contains invalid data.

