from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + " || " + self.email + " || " + self.contact
    
class Service(models.Model):
    address = models.CharField(max_length=20)
    salary = models.CharField(max_length=50)
    city = models.CharField(max_length=12)
    state = models.CharField(max_length=100)
    union_territories = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.address + " || " + self.salary + " || " + self.city
    
class Login(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username + " || " + self.email