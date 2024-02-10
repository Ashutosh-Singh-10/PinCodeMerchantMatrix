from django.db import models


class PinOrdered(models.Model):
    pinCode=models.IntegerField() #work as primary key in B+tree
    merchantId=models.IntegerField()
    
class MerchantOrdered(models.Model):
    merchantId=models.IntegerField() #work as primary key in B+ tree
    pinCode=models.IntegerField()

