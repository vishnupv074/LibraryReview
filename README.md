# LibraryReview
This app is for listing libraries and their reviews. Users can view and add review. Admin can manage
reviews, libraries etc.

# Installation

To install this in local server after downloading and extracting the repo.

1. Create a python 3.7 virtualenv and activate
2. Then run
    ```commandline
   cd LibraryReview
   pip install -r requirements.txt
    ```
3. Initialize database
    ```commandline
   python manage.py makemigrations
   python manage.py migrate
    ```
4. Create superuser
    ```commandline
   python manage.py createsuperuser
    ```
5. Then run
    ```commandline
   python manage.py runserver
    ```
