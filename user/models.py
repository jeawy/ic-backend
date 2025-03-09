from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " | " + self.email + " | " + self.phone + " | " + self.department + " | " + self.role
        