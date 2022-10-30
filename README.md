# BE-SEM7-Projects-NLP

# Django Project Setup Guide

Django allows us to build powerful web applications in a relatively short time. This guide is an attempt to help you setup your Django project on your local machine. We will be going through pip, virtualenv,virtualenvwrapper and more.

## Install virtualenv & virtualenvwrapper

When we install Django, it's not ready for production at all. The settings for a production ready Django project is different from a development environment. If you are new to Django or building web applications in general this can seem frustrating, but it's important to know how you set up your Django project.

The standard for Django projects is to isolate them inside of virtual environments. This way we prevent dependencies to conflict with each other if we're working on multiple projects.

Virtualenv is a tool to create such environments. You can install it by using pip:

```
$ pip install virtualenv
```

Next thing we need to install is virtualenvwrapper. Virtualenvwrapper is a set of extensions to virtualenv. We need this to set up different working environments for our Django settings later. With virtualenvwrapper we can tell which django settings module it should use when the environment is activated.

Install virtualenvwrapper using pip:
```
$ pip install virtualenvwrapper
```
or your package manager if you're on Linux. Below an example if your on Ubuntu:
```
$ sudo apt install virtualenvwrapper
```

## Creating our virtual environment
In your terminal type `$ which python3` to know your Python3 path. In my case it was:
```
$ /usr/bin/python3
```
We are going to use Python3 as our default Python for our Django projects. Create a virtual environment with the following command:
```
$ mkvirtualenv --python=/usr/bin/python3 nlp
```
You can replace `nlp` with whatever you like. Make sure it makes sense though. We named this one *nlp* because we are going to use this for our development working environment.

After creating your virtual environment your terminal should show something like:
```
(nlp)user@host $
```
If you wish to exit out of your virtual environment simply type `$ deactivate` in your terminal.

To activate type:
```
$ workon nlp
```
If you type `$ workon` and press enter, it will return all the virtual environments you have created using the `$ mkvirtualenv` command.

Now we install Django and set up our project.

## Install And Setup Django Project

While your virtualenv is active install Django using pip:
```
$ pip install Django
```
You can specify which Django version you want to install. For example:
```
$ pip install Django==4.1.2
```

Clone the project from https://github.com/AditChheda/BE-SEM7-Projects-NLP

Run the development server to check if everything has been installed correctly:
```
$ python manage.py runserver
```

You can open your favorite browser and check at `http://127.0.0.1:8000/`.
