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
- Added 3 test notes through admin, one in each category.
- Created `NoteAdmin` class with categories `title`, `category`, `created`, `updated` in `notesapp/admin.py`
- Checked `http://127.0.0.1:8000/notes/` for the existing notes.
- Added `Postman VSCode Extension`.
- Created `note_detail` function in `notesapp/views.py` to handle GET, PUT and DELETE requests regarding note details and error responses. 
- Added to urls.py - path("notes/<slug:slug>/", views.note_detail, name="note_detail"),
- Used Postman Extension to POST a new note.

## Block 4 - REACT SIDE (FRONTEND)




