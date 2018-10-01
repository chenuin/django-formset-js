from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length = 128, verbose_name = 'Name')
    phone = models.CharField(max_length=32, verbose_name='Phone')
    email = models.EmailField(max_length=256, verbose_name='E-mail')
