# StudentPortal

A containerized web application for managing student records. We use Docker Compose to create a seamless environment for the application and ensure data persistence through Docker volumes.

## Directory Structure
```
├───app
│   │   app.py
│   │   Dockerfile
│   │   requirements.txt
│   │
│   └───templates
│           add_student.html
|
└───db
        init.sql
```

## Application Components

- **docker-compose.yml**: Configuration file for Docker Compose, defining services and their interconnections. It sets up the environment for the application, including an app service and a database service.

- **init.sql**: SQL initialization script responsible for creating the necessary database and table structures, as well as inserting initial data.

- **Dockerfile**: Instructions for building a Docker image for the Flask web application. It specifies the base image, exposes ports, copies application files, installs dependencies, and sets the command to run the app.

- **app.py**: The main Python script that powers the Flask web application. It handles database connections, data retrieval, and JSON responses.

- **add_student.html**: An HTML template for a web page that allows users to input student data.

## Running the Application
Build and run the containers in daemon mode using the following command:

```
docker-compose up -d --build
```

- To access the application, open your web browser and go to [localhost:5000](http://localhost:5000). You will be greeted with a welcome message.

- To view existing student data from the database, navigate to [localhost:5000/student_data](http://localhost:5000/student_data).

- If you want to insert new student records, visit the [`localhost:5000/add_student_form`](http://localhost:5000/add_student_form) route.

The database will be stored inside the data folder, ensuring data persistence.