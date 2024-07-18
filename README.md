# Contact-list
## Overview

The Contact List Application is a web-based solution for managing personal and professional contacts.
It allows users to create, update, delete, and view contacts with ease. The application is built using Django and Docker for containerization.

## Features

- User authentication and authorization
- CRUD operations for managing contacts
- RESTful API for interacting with contacts
- Docker support for easy deployment

### Prerequisites

- Python 3.x
- Docker

### Installation

 1-Clone the repository:


    ```
    git clone https://github.com/yourusername/Contact-list-main.git
    cd Contact-list-main
    ```
### Using Docker

1. Build and run the containers:

    ```sh
    docker-compose up --build
    ```

2. Access the application at `http://localhost:8000`.

### Services

The Docker setup consists of the following services:

- **web**: This service runs the Django application.
- **db**: This service runs a PostgreSQL database.

### Default Admin User

After running the application with Docker, a default admin user is created with the following credentials:

- **Username**: `taha@admin.com`
- **Password**: `taha123`

You can log in to the Swagger interface at `http://localhost:8010/swagger/` using these credentials.

## Usage

- Register an account or log in if you already have one.
- Create, update, delete, and view your contacts.
## Endpoints

Below are the endpoints available in the Contact List Application:
#### Contacts

- **POST /contact/generate/**: Generate a new contact.
- **GET /contact/retrieve_list/**: Get a list of all contacts.
- **PUT /contact/update_contact_detail/{detail_id}/**: Update an existing contact.
- **DELETE /contact/delete_contact/{detail_id}/**: Delete a contact.
#### Authentication

- **POST /auth/token/**: Obtain a JWT token.
  - Request body: `{"username": "string", "password": "string"}`
  - Response: `{ "access": "JWT access token", "refresh": "JWT refresh token" }`

- **POST /auth/token/refresh/**: Refresh the JWT token.
  - Request body: `{"refresh": "JWT refresh token"}`
  - Response: `{ "access": "new JWT access token" }`
  
- **POST /auth/register/**: Register a new user.
  - Request body: `{ "password": "string", "email": "string"}`

  
