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



**Feedback is welcome from everyone**

## Get app running on local machine

You need to have Docker installed on your machine.

From the repo root, run the following commands:

```bash
cd build
docker-compose up
```

This will spin up the containers and serve the application at http://localhost:8000/.
