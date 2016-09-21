## Vitabu
A book inventory management application.

## What is it?
An app that enables one to save books according to name and category.
Users can search for a book by its name, category or both name and category.

## The latest version
The latest version is 1.0

## How to install and setup the project
Clone the repo.
```
git clone git@github.com:alexkiura/vitabu.git
```

Navigate to the root folder
```
cd vitabu
```

install the necessary packages
```
pip install -r requirements.txt
```

Perform migrations by running
* `python manage.py makemigrations`
* `python manage.py migrate`


## Testing
To test the app, run
```
python manage.py test
```

Create an admin by running
```
python manage.py createsuperuser
```

Run the server
```
python manage.py runserver
```

Add some sample books on the [admin](http://localhost:8000/admin/) page

Test out the search functionality [here](http://localhost:8000/)
