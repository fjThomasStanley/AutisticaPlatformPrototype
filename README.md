# Autistica Platform Prototype

## Background


This repository is linked to the [Autistica citizen science project repository](https://github.com/alan-turing-institute/AutisticaCitizenScience). This repository contains the code for the platform prototype. This prototype for the Autistica Citizen Science platform has been developed utilising the Python [Django](https://www.djangoproject.com/) web development framework. 


## Releases

The most recent version of the prototype is available at: http://deplo-autis-udrg410qq9qr-1321397698.eu-west-2.elb.amazonaws.com/.




## Three tier application architecture

###  What is a three tier application achitecture?

A three tier application achitecture refers to a concept of delivering an application to end users via three different modular layers consisting usally of:

- Presentation tier: The application is presented to the application user. When referring to web applications, this is usually presented graphically in the user's web browser. 
- Application tier: The logic of the application is processed here. This tier builds or renders the information required by the presentation layer. The application layer usually talks to the Data tier to store and retrieve user information. 
- Data tier: Where user information is held and accessed by the application tier

A three tier achitecture is also known as a client-server application as the presentation tier (client) rely on the application and database tiers (server) for access to the application data.  



### Why this project needs a three tier architecture?

This project requires a three tier achitecture primarily because   in a safe and secure way




### How does this project utilise the three tier achitecture model?

The prototype is delivered via a three tier web architecture consisting of:

- Web Browser (Presentation tier) - The visual display of the platform application to the user in the client web browser 
- Application Server (Application tier) - The application logic on the web server to render the website files such as the HTML to be sent to the cient
- Database (Data tier) - Persistance of user data in a database 

Different kinds of technologies and platforms are used at each tier of the web architecture:

- Web Browser:
    - Browser platform - Chrome, Firefox, Safari, Edge etc.
    - Website code - HTML, JavaScript, CSS

- Application Server:
    - Web development frameworks - Django
    - Code - Python, HTML (Django Templates)
    - Server Architecture - e.g. Cloud based hosting such as Amazon AWS or Heroku

- Database - [Open Humans](https://www.openhumans.org/)


## Code Structure

Structuring code in a logical way in a project is very important as poor code structuring can very quickly lead to a completely unmanagemable mess. When we talk about Code Structuring we are simply referring to how code (or any kind of resource that makes up a project) is stored and constructed. For example code structuring will define what kinds of files make up a project, where these files should be located based on their individual purpose within the project and finally how the files should be written. 

### Why we need code structure

Having an established code structure that follows software development best practice is key to ensuring the maintainability and readability of a project. Maintainability is a characteristic of a project that determines how easy it is for developers to find and fix problem code. In software development we should always strive to keep the project in a good maintainable state as this will help developers of the project to fix problems with the code.

Good code readibility is a characteristic of a maintainable software. By having readable code, software developers of different backgrounds, experience and familiarity with the codebase should be able to understand how the project code fits together and the reasoning as to why a particular piece of code is required (its purpose within the project).

### how we achieve code structure

In the platform prototype project good Code structure is achieved by maintaing a hierachy of files and folders. 

This project is based on the web framework of Python Django and because of this the project inherits the base code structure that Django creates when a project is initiated using the Django CLI (Command Line Interface) tooling. 

- Root
    - locale
    - main_app
    - skeleton (the root of the entry django app)
    - static (Website resources such as images and styling files - CSS)



Another important Component based development approach


Styling CSS!!

Global and Private - To reduce the duplication of CSS within the platform 


**Feedback is welcome from everyone**

## Get app running on local machine

You need to have Docker installed on your machine.

From the repo root, run the following commands:

```bash
cd build
docker-compose up
```

This will spin up the containers and serve the application at http://localhost:8000/.
