from django.db import models

# Create your models here.


class Authentication(models.Model):
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    withPic = models.CharField(max_length=300)

class Meta:
    verbose_name_plural = "Users"

