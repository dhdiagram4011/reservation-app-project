from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    address_01 = models.CharField(max_length=200)
    address_02 = models.CharField(max_length=200)
    #created_date = models.DateTimeField(auto_now_add=True)
    #published_date = models.DateTimeField(null=True, blank=True)


