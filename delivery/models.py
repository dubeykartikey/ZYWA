from django.db import models

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    card_id = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)


class CsvFiles(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to='data/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    