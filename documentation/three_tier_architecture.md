# Three tier application architecture

##  What is a three tier application achitecture?

A three tier application achitecture refers to a concept of delivering an application to end users via three different modular layers consisting usally of:

- Presentation tier: The application is presented to the application user. When referring to web applications, this is usually presented graphically in the user's web browser. 
- Application tier: The logic of the application is processed here. This tier builds or renders the information required by the presentation layer. The application layer usually talks to the Data tier to store and retrieve user information. 
- Data tier: Where user information is held and accessed by the application tier

A three tier achitecture is also known as a client-server application as the presentation tier (client) rely on the application and database tiers (server) for access to the application data.  



## Why this project needs a three tier architecture?

This project requires a three tier achitecture primarily because the goal of the application is to collect user information (experiences) and securely and safely this information with other relevant stakeholders such as researchers and other platform users. A three architecture is secure in that the application and data tiers are managed centrally and therefore application updates to all users can be deployed very quickly. Central management of the application and data tiers ensures data access is moderated by user account information.  


Another benefit to a three tier architecture is that each tier of the application stack can be developed and managed independently. For example the application tiers and data tiers are developed and managed seperately; application tier is developed and managed by The Alan Turing Institute, the data tier is developed and managed by OpenHumans. This seperation of development is great, particularly in a collaborative development approach, because collaborators can focus on a particular technical aspect of the platform that best utilises their skills.


## How does this project utilise the three tier achitecture model?

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