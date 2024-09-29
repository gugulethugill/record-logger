# **Fullstack Application: Flask + React**

This project is a simple fullstack application that utilizes Flask as the backend and React as the frontend. The application allows users to submit and retrieve records via a RESTful API.

# **Prerequisites**
Backend (Flask):

Python 3.7 or later, Flask, Flask-CORS (for handling CORS)

Frontend (React):

Node.js (v14 or later), npm (Node Package Manager)

# **Install Frontend Requirements**

$ npm install

# **Install Backend Requirements**

$ brew install virtualenv

$ virtualenv env

$ source env/bin/activate

$ pip install flask

$ pip install -U flask-cors

$ npm install axios --save

# **Run Backend**

$ flask run -p 5001

# **Run Frontend**

Ensure the backend is running first

$ npm start

Open your browser to http://localhost:3000

You can then interact with the application by adding records and retrieving the last inserted record.
