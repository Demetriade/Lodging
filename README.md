# Lodging App

Lodging is a web application to help the owner of lodges to cummunicate with their lodgers.
<br />Also, the lodgers can communicate between them without accessing to their private information.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.
<br />**It is recommended to install these in a python virtual environment.

```bash
#Install virtualenv and create one
pip install --user virtualenv   
virtualenv venv

#Activation for mac/linux
source venv/bin/activate

#Activation for windows
venv\Scripts\activate

#Packages for the project
pip install django              #Framework for web app
pip install pillow              #For the ImageFields
pip install django-crispy-forms #Enchanced the style of forms

```

## Run

```bash
source venv/bin/activate
python manage.py runserver
```
