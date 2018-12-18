from django.db import models

# Create your models here.
class creditcard(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.EmailField()
    CardNumber=models.IntegerField()
    SecurityNumber=models.IntegerField()
    Zipcode=models.IntegerField()

class accesscodes(models.Model):
    CodeNumber=models.IntegerField()
    id=models.IntegerField(unique=True,primary_key=True)
