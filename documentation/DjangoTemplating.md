## Django Templating system - How are platform components written and used?

The platform utilises Django's templating system so that common or repeatable sections of code can be written once in a generic template and then reused or included in a parent page. 

## Include
In order to include Django templates or components within a parent page we must utilise the Django include tag:  

```
{% include 'pathToComponentTemplate' %}
```

Some components have parameters which can be utilised to customise the appearance and content. As part of the Django include statement we can use the 'with' keyword to assign a value to a component template paramter name:  

```
{% include 'pathToComponentTemplate' with componentParameterName=value %}
```

More than one parameter can be defined on the include tag which is useful if more than one parameters on a template needs to be defined:  

```
{% include 'pathToComponentTemplate' with componentParameterName=value anotherParameterName=secondValue %}
```

Django Parameter values can be specified as a static string or we can use a data object as passed in via the context variable of the views.py render function. This second method using the context variable is particulary useful as we can allow the template to adjust to user data such as profile settings.  

## Extends

The Django templating system also allows for the functionality of extending base templates. This is very useful as multiple components that are similar can derive from one singular template and only the differences amongst the collection of similar components need to have a separate template file. The concept of 'DRY' (Don't repeat yourself) whereby the code structure is setup and written such that code is only written once is very important as it significantly contributes to the maintainability characteristics of a software project. Because Django includes the template extension tag, it allows us to follow 'DRY' principle when writing templates.  


```
{% extends 'pathToComponentTemplate' %}
```

```
{% include 'pathToComponentTemplate' %}
```

## For

Another Django tag that allows us to follow 'DRY' principles is the for tag. Whereas the extends tag allows us to keep to DRY principles for a whole template, the for tag allows us repeat over a generic code block within a template. This allows us to reduce the size of templates as only a generic code block required than manually repeating the code block over and over in the template. The for tag is useful in scenarios such the display of a table where an array of user data can be passed into the template and the for loop will automatically loop over the data and generate a row in the table for each item in the data array. Django for loops allow us to make templates dynamic with respect to user data.  

```
{% for %}
```

## Full Django Documentation

There are other Django templating tags and features which can be found [here](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/). For other Django related documentation please see [here](https://docs.djangoproject.com/en/3.0/).