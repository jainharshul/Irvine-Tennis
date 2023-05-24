# Irvine-Tennis

Project Description:

The project is a customer management application developed using Flask, a web framework for Python. The application allows users to submit customer information, generate unique customer IDs, and perform various operations related to customer management.

The project consists of several files and functionalities:

main.py: This file is the main entry point of the application. It sets up the Flask app and defines the routes for different pages. The routes handle HTTP requests and render the corresponding HTML templates. The main functionalities include submitting customer information, generating unique customer IDs, updating customer details, and marking customers as completed.

customer class: This class defines the structure of a customer object. It contains attributes such as the customer's name, type, tension, date, phone number, payment information, and a unique ID. The class methods handle the generation of a random ID and the storage of customer objects.

Templates (text.html, index.html, print.html, updatecustomer.html, fail.html, done.html): These HTML templates define the user interface of the application. They provide a visually appealing and interactive environment for users to enter and view customer information. The templates are rendered by the Flask routes and display the appropriate data.

Various route functions: The Flask routes handle different functionalities of the application. For example, the "/submit" route processes the customer information submitted via a form, generates a unique ID, stores the customer object, and renders the "updatecustomer.html" template with the customer details. The "/done" route marks a customer as completed based on the provided ID.

The project demonstrates proficiency in web development using Flask. It showcases the ability to handle HTTP requests, render dynamic HTML templates, and manage data storage and retrieval. The application provides a convenient solution for managing customer information, generating unique IDs, and tracking customer statuses.

Through this project, I gained experience in building interactive web applications, handling form submissions, and implementing data storage and retrieval using Flask. The project highlights my skills in web development, backend programming, and problem-solving.

Overall, the customer management application project demonstrates my ability to create functional and user-friendly web applications using Flask. It showcases my expertise in web development technologies and my capability to design and implement practical solutions.
