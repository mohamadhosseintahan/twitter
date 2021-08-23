# twitter
### This is a twitter like app back end that developed by django and djangorestframework

### We used celery for async tasks like sending email to users for daily report and also we used elasticsearch for indexing tweets.

## how to run
```
pipenv install -r requirements.txt
```
The following command might be encounter with error in windows.
then:
```
python manage.py runserver [-p] 
```
-p is optional. it's for port. if you refuse to use that, it will be set 8000 by default.
