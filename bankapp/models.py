from django.db import models

# Create your models here.
class Banking(models.Model):
    c_name=models.CharField(max_length=15)
    c_id=models.IntegerField()
    c_phone_no=models.BigIntegerField()
    c_emailid=models.EmailField()
    c_balance=models.FloatField()
