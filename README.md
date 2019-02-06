# PYTHON AND JENKINS

## Create a local project
* Create a project with your IDE (suggested PyCharm)
* Open local project folder and run
```
virtualenv -p python3 env
```
* Change IDE interpreter to point this new virtualenv
* Create a README.md file where put all your main documentation
* Create a requirements.txt file where put all your python dependencies
* Let's write some python code

## Create a base Django webapp
* Add to your requirements file, for example:
```
Django==2.1.5
```
* (not required) Or install directly latest Django version in your virtualenv
```
pip install django
```
* Automatically create a new django project "mywebapp" folder structure
```
django-admin startproject mywebapp
```
* Add an app "items". Because as per doc: An app is a Web application that does something – A project is a collection of configuration and apps for a particular Web site. A project can contain multiple apps. An app can be in multiple projects.
```
cd mywebapp
python manage.py startapp items
```
* Add "items" as installed app of your project in settings.py
```
INSTALLED_APPS = (
    ...
    'items',
)
```
* Setup database
```
python manage.py makemigrations
python manage.py migrate
```
* Crete a simple view in "items/views.py"
```
from django.http import HttpResponse


# simplest view possible
def home(request):
    return HttpResponse("Hello, world. You're at the Items-app homepage.")
```
* Bind that view to your "items" app in "items/urls.py"
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
* Bind your "items" app to your "mywebapp" project in "mywebapp/views.py"
```
urlpatterns = [
    path('items/', include('items.urls')),
    ...
]
```
* Run and test using a browser looking for "http://127.0.0.1:8000/items/"
```
python manage.py runserver
```
* (not required) To avoid an ugly /favicon.ico - 404 NOT FOUND, add to "items/urls.py" and add a file like "items/static/favicon.ico"
```
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    ...
    re_path(r'^favicon\.ico$', favicon_view),
    ...
]
```