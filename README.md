Movie Database API with Django
This repository contains a simple Django backend for managing a movie database. The backend provides APIs for retrieving, adding, updating, and deleting movies, as well as custom filtering options.

Features
Relational Database Schema: The backend utilizes a relational database schema to manage movie data efficiently. It includes proper relationships between different models such as movies, genres, actors, technicians, etc.
API Endpoints:
GET and POST APIs for Movies: Fetch a particular movie or add/update a movie.
GET API for All Movies: Retrieve all movies, paginated for better performance. Includes custom filters to fetch movies based on actors, directors, technicians, or combinations thereof.
POST API to Delete Actors: Deletes an actor from the database if they are not associated with any movies, ensuring data cleanliness.
Technologies Used
Django Framework: The backend is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST Framework: Utilized for creating RESTful APIs in Django, providing powerful tools for serialization, authentication, and permissions.
ORM (Object-Relational Mapping): Django's built-in ORM is employed to interact with the database, abstracting away the need to write SQL queries directly.
Getting Started
To run the backend locally:

Clone this repository to your local machine.
Install Python and Django if you haven't already.
Navigate to the project directory in your terminal.
Run python manage.py migrate to apply migrations and create the database schema.
Start the development server with python manage.py runserver.
Access the API endpoints through a tool like Postman or your browser.
Contribution
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.