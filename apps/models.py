from django.db import models


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    text = models.TextField()