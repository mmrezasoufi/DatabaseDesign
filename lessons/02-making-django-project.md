## Install Django
```bash
pip install django
```
## Create Django Project
```bash
django-admin startproject <project-name> <optional-path>
```
## Make an app
```bash 
python manage.py startapp <app-name>
```
**important:** Add the app name to the `INSTALLED_APPS` list in `settings.py` file.
## Change static roots
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
## Collect static files
```bash
python manage.py collectstatic
```
## Make migrations
```bash
python manage.py makemigrations # FOR WRAPPING UP THE CHANGES IN MIGRATION FILES OF THE APPS
```
## Migrate
```bash
python manage.py migrate # FOR APPLYING THE MIGRATIONS TO THE DATABASE
```
## Create superuser
```bash
python manage.py createsuperuser
```
## Run server
```bash
python manage.py runserver <optional-host>:<optional-port>
```
