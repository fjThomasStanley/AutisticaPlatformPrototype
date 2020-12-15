## Folders

| FolderName       | Purpose     |
| :-------------   | :---------- |
|  migrations      |  Contains all the Django Migration files in order to setup the Django models in the database  | 
|  old             |  This project is forked from the [Autistica-Filemanagement-Demo](https://github.com/alan-turing-institute/autistica-filemanagement-demo). This folder contains the templates used by the original project.   |
|  templates       |  Contains all the template files for the project components | 
|  templatetags    |  Contains custom Django python functions to extend the base set of Django templating tags. For example additional template filters can be held here. |
|  tests           |  Any test automation testing scripts can be held here |


## Files

| FileName       | Purpose      | 
| :------------- | :----------  |
| admin&#46;py   |  Sets up the configuration of the Django administration site |
| apps&#46;py    |  Sets up the code in the current directory as a Django app |
| models&#46;py  |  Specifies the Django models required by the Django app |
| urls&#46;py    |  Specifies the available URL that can be used by the Django app |
| views&#46;py   |  Specifies the Django view functions that are accessed by via the URLs&#46;py to render the Django templates|
