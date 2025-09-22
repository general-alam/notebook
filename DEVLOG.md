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
- Created initial `Note` model in `models.py` with fields:
  - `title` → `CharField`
  - `body` → `TextField`
  - `slug` → `SlugField` (unique)
  - `category` → `CharField` with choices (`WORK`, `PERSONAL`, `IMPORTANT`)
  - `created` → `DateTimeField(auto_now_add=True)`
  - `updated` → `DateTimeField(auto_now=True)`

