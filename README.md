##  A simple Chat App 


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/simple_book_api.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install virtualenv [here](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3#:~:text=Virtualenv%20is%20a%20tool%20used,the%20globally%20installed%20libraries%20either).)

After installation create a virtual environment by running:

```sh
$ virtualen env_name
```

Next, activate the virtual enviroment with :

```sh
$ source env_name/bin/activate
```

## Without Docer
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Use migrate command to effect database model:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Start the server with:
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


## With Docker
```sh
sudo docker-compose up --build
```


### Useful resources

- [Django Environ](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)


