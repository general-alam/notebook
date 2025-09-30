## Block 1: Project set-up
- Followed Django docs: https://docs.djangoproject.com/en/2.2/howto/windows/
- Installed virtual environment tools:
  - `pip install virtualenvwrapper-win`
  - `mkvirtualenv myproject`
- Installed Django inside the virtualenv:
  - `pip install django`
- Created Django project:
  - `django-admin startproject notebook`
- Created app (must differ from project name):
  - `python manage.py startapp notesapp`
- Opened VS Code in project folder with `code .`
- Verified server works:
  - `python manage.py runserver 8004`

## Block 2: App Registration & Models
- Added `notesapp` to `INSTALLED_APPS` in `settings.py`
- Created initial `Note` model in `models.py` with fields (`title`, `body`, `slug`, `category`, `created`, `updated`)
- Created  `save` function to create a unique slug for urls on the first save in `models.py`.
- BUG: Had not realised I'd forgotten relevant imports (`slugify, get_random_string` from `django.utils`) in `models.py` until later running code. 
- Ran the initial migrations 
  -> This sets-up Django's default database, while running these commands again commits any changes in `models.py` to keep things in sync
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Created admin superuser for testing 
  - `python manage.py createsuperuser`
  - details -> user: user, password: password
- Ran server, and logged into admin to check it works:
  - `python manage.py runserver`
  - at http://127.0.0.1:8000/admin/
  - `Notesapp` appeared as a Model, with Notes, Add, Change all present. 
  - Sucessfully created a test note with all fields. 
  - Sucessfully updated the test note. 
  - Note kept after re-running server.
  - Sucessfully deleted the test note and re-ran server to check. 

## Block 3
