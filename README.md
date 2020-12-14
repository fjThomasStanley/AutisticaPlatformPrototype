# Autistica Platform Prototype

## Background


This repository is linked to the [Autistica citizen science project repository](https://github.com/alan-turing-institute/AutisticaCitizenScience). This repository contains the code for the platform prototype. This prototype for the Autistica Citizen Science platform has been developed utilising the Python [Django](https://www.djangoproject.com/) web development framework. 


## Releases

The most recent version of the prototype is available at: http://deplo-autis-udrg410qq9qr-1321397698.eu-west-2.elb.amazonaws.com/.


## Design Decisions

To understand the full reasoning and justification behind the design decisions for the platform, please refer to the [Design Decisions Document](./documentation/COMPONENT_DESIGN_DECISIONS.md). 

**Feedback is welcome from everyone**

Please understand that the design of the platform has been fundamentally influenced by the community and their feedback into the project development. Community input is key to the development of this project and so if you would like to get involved please refer to this [Get Involved Document](https://github.com/alan-turing-institute/AutisticaCitizenScience/blob/master/get-involved/README.md).   

## Navigating the prototype views

### Index

The index view displays the application prototype on its own. The index view can be accessed via:

[Root of application URL]/

e.g. localhost:8000/

or 

[Root of application URL]/index

e.g. localhost:8000/index



### Gallery

The gallery view displays all the individual components of the application split apart independently. The gallery documents the purpose of each components and how it can be technically used on the platform application. This view is more usefull for those developing the platform or those who wish to provide feedback for a specific component on the platform. The gallery view can be accessed via:

[Root of application URL]/gallery

e.g. localhost:8000/gallery


### Split

The split view diplays both the index and gallery views together side by side; usefull for those developing the platform or those who wish to provide feedback for a specific component on the platform. The split view can be accessed via:

[Root of application URL]/gallery

e.g localhost:8000/split

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


## Get app running on local machine

You need to have Docker and Docker Compose installed on your machine.

From the repo root, run the following commands:

```bash
cd build
docker-compose up -d
```

This will spin up the containers and serve the application at http://localhost:8000/.

To shutdown the application, in the same build directory please run:

```bash
docker-compose down
```

To confirm which docker applications (containers) are running on your machine please run:

```bash
docker ps -a
```

