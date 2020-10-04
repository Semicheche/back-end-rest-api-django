# back-end-rest-api-django
##
- [Python 3](https://www.python.org/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [MongoDB](https://www.mongodb.com/)

## Get Starting (Linux/MacOS)
Install `virtualenv` to create a isolated environment to the project:
```
$ pip install virtualenv
```
Then on folder where stay the application create the virtual environment
```
$ virtualenv env
```
Then only activate with this command:
```
$ source env/bin/activate
```
Now clone repositories with project:
   ```
   $ git clone https://github.com/Semicheche back-end-rest-api-django.git
   ```
After repository cloned run this command:
```
$ cd back-end-rest-api-django
```
Into the folder **back-end-rest-api-django** run this command:
```
$ pip install -r requeriments.txt
```
After install all requeriments configure Database connection on `ApiRestProduct/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'database_name',
        'HOST': 'host',
        'PORT': 27017,
    }
}
```
then just run the migrate

```
$ python manage.py migrate
```
And is ready to run application:
```
$ python manage.py runserver
```




