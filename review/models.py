from django.db import models


# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    review = models.TextField()
    guest = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    is_approve = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

