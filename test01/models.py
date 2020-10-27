from django.db import models

# Create your models here.
# class item_klass(models.Model):
#     pass

class Test(models.Model):
    name = models.CharField(max_length=20)