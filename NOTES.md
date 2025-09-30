## Models
- SlugField: generates user-friendly part of URL instead of original ID (eg. '1' -> 'contact-us')

## Migrations 
[Reference documentation](https://docs.djangoproject.com/en/5.2/topics/migrations/)
- It's how django propagates changes to models (adding fields/deleting models) in the database. 
- Commands: 
    - `migrate` (applying/unapplying migrations)
    - `makemigrations` (creating new migrations based on changes make to models - similar to commits)
    - `sql migrate` (displays dql statements for a migration)
    - `showmigrations` (lists project's migrations and their status)
- Most capable backend support option: `PostgreSQL`
- Workflow: 
    1. Make changes to your model, then run: `python manage.py makemigrations`. Check if it's what you intended. (You can add a more meaningful name by following format `python manage.py makemigrations --name changed_my_model your_app_label` instead.)
    2. Apply them to your database to make sure they work as expected: `python manage.py migrate`
- [Reversing migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/#reversing-migrations)
    


