# Autistica Platform Prototype

## Background


This repository is linked to the [Autistica citizen science project repository](https://github.com/alan-turing-institute/AutisticaCitizenScience). This repository contains the code for the platform prototype. This prototype for the Autistica Citizen Science platform has been developed utilising the Python [Django](https://www.djangoproject.com/) web development framework. 


## Releases

The most recent version of the prototype is available at: http://deplo-autis-udrg410qq9qr-1321397698.eu-west-2.elb.amazonaws.com/.


## Design Decisions

To understand the full reasoning and justification behind the design decisions for the platform, please refer to the [Design Decisions Document](./documentation/COMPONENT_DESIGN_DECISIONS.md). 

This application uses a three tier achitecture for delivery. To read more technical information about what three tier archticture is and why this project utilises it, please read the [Three Tier Architecture Document]()

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

