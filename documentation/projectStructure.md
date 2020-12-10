# Project Structure

Structuring code in a logical way in a project is very important as poor code structuring can very quickly lead to a completely unmanagemable mess. When we talk about Code Structuring we are simply referring to how code (or any kind of resource that makes up a project) is stored and constructed. For example code structuring will define what kinds of files make up a project, where these files should be located based on their individual purpose within the project and finally how the files should be written. 

## Why we need code structure

Having an established code structure that follows software development best practice is key to ensuring the maintainability and readability of a project. Maintainability is a characteristic of a project that determines how easy it is for developers to find and fix problem code. In software development we should always strive to keep the project in a good maintainable state as this will help developers of the project to fix problems with the code.

Good code readibility is a characteristic of a maintainable software. By having readable code, software developers of different backgrounds, experience and familiarity with the codebase should be able to understand how the project code fits together and the reasoning as to why a particular piece of code is required (its purpose within the project).

## How is code structure implemented in this project

In the platform prototype project good Code structure is achieved by maintaing a hierachy of files and folders. 

This project is based on the web framework of Python Django and because of this the project inherits the base code structure that Django creates when a project is initiated using the Django CLI (Command Line Interface) tooling. 

This file refers to the 1st level structure of the repository [root](/)


### Folders

| FolderName       | Purpose     |
| :-------------   | :---------- |
|  build           |  Contains files for deploying the prototype to docker using docker-compose  | 
|  documentation   |  Contains documentation for the prototype platform  |
|  images          |  Contains any images that are used | 
|  locale          |  Contains language translation files used by the platform to support user language selection preferences (e.g. English, French, German, Spanish) |
|  main_app        |  The entry point Django App, the application is started from this |
|  skeleton        |  The main Django app for the platform prototype |
|  static          |  Contains all content and assets the platform depends upon e.g application scripts, styling (CSS), images etc.|

### Application Django Apps

| FolderName        |
| :-------------    |
| stepperComponent  |

### Files

| FileName       | Purpose      | 
| :------------- | :---------- |
| .hound.yml     | Configuration file for the Hound code review service. Specifies how Hound should review the codebase. |
| .travis.yml    | Configuration file for the TravisCI automation testing service. Specifies how TravisCI should be setup in order to conduct a test of the codebase. |
| db.sqlite3     | Used to store Django models |
| env.sample     | An example environment file to correctly setup integration between this platform and the OpenHumans service for data storage|
| LICENSE        | The type of software license this project is using to inform those who interact with this project and its codebase the legal terms upon which must adhere to |
| manage&#46;py      | Django administration |
| Pipfile        | Specifies project Python dependencies |
| Pipfile.lock   | Specifies project Python dependencies |
| Procfile       | Heroku configuration |
| README&#46;md | Project description file. Human readable to explain |






### Styling

Another important Component based development approach

Styling CSS!!

Global and Private - To reduce the duplication of CSS within the platform 






