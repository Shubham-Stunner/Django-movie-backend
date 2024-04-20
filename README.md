# Django Movie Backend

Welcome to the Django Movie Backend repository! This backend is designed to manage a movie database, providing APIs for various CRUD operations and custom filtering options.

## Overview

The backend is built using Django, a high-level Python web framework. It leverages Django's powerful features such as the ORM for interacting with the database and Django REST Framework for creating RESTful APIs.

## Features

- **Relational Database Schema**: The backend utilizes a relational database schema to manage movie data efficiently. It includes proper relationships between different models such as movies, genres, actors, technicians, etc.
  
- **API Endpoints**:
  - **GET and POST APIs for Movies**: Fetch a particular movie or add/update a movie.
  - **GET API for All Movies**: Retrieve all movies, paginated for better performance. Includes custom filters to fetch movies based on actors, directors, technicians, or combinations thereof.
  - **POST API to Delete Actors**: Deletes an actor from the database if they are not associated with any movies, ensuring data cleanliness.

## Getting Started

To run the backend locally:

1. Clone this repository to your local machine.
2. Install Python and Django if you haven't already.
3. Navigate to the project directory in your terminal.
4. Run `python manage.py migrate` to apply migrations and create the database schema.
5. Start the development server with `python manage.py runserver`.
6. Access the API endpoints through a tool like Postman or your browser.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
