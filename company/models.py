from django.db import models

# Create your models here.
class Company(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('disabled', 'Disabled'),
    ]
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.name + " | " + self.email + " | " + self.phone + " | " + self.address