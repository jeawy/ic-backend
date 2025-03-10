from django.db import models
from company.models import Company

# Create your models here.

class Broker(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='brokers')
    license_no = models.CharField(max_length=100)
    license_issued_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')

    # need to still add performance statistics and commissions into the model field

    def __str__(self):
        return self.first_name + " | " + self.last_name + " | " + self.email + " | " + self.phone + " | " + self.address + " | " + self.company.company_name + " | " + self.license_no

