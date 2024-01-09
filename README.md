# Django Task Backend

Django Task Backend is a small project for storing daily tasks. I was mainly interested in testing the power of Django without using any extension to make a restful backend service.

### Features

- Register endpoint for new users
- Login endpoint for existant users
- After logging in, the response is a JWT to be able to create new tasks or check existing ones
- Each user has unique tasks that can be accessed by the owner of the tasks

## Requirements

- Python 3.11+
- SQLite
- http client: POSTMAN, Insomnia, cURL

### Running Locally

```
git clone https://github.com/Edmartt/django-task-backend.git
```

or ssh instead:

```
git clone git@github.com:Edmartt/django-task-backend.git
```

browse into project directory:

```
cd django-task-backend/
```

create virtual environment

```
python -m venv env
```
activate virtual environment

```
. env/bin/activate 
```
install dependencies

```
pip install -r requirements.txt
```

set environment variables following the [.envrc.example](https://github.com/Edmartt/django-task-backend/blob/main/.envrc.example) file and run

```
python manage.py runserver
```


#### Note

api documentation in: `/api/v1/swagger`