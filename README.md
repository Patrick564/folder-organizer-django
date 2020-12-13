# Folder-organizer (Django)

A page for organize multiple folders with specific fields as Name, Serie, Code, etc.
See an example in Heroku [here](https://folder-organizer.herokuapp.com/)

## Instalation

First create a virtualenv, name it '.venv' or as you like.

```bash
python3 -m venv .venv
```

Activate the virtual enviroment.

```bash
source .venv/bin/activate
```

Then install requirements.

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file and/or a local_settings.py file, continue with the migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser.

```bash
python manage.py createsuperuser
```

And run server

```bash
python manage.py runserver
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
