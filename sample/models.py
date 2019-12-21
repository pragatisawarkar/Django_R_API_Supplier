from django.db import models

# Create your models here.
class Address(models.Model):
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    active=models.CharField(max_length=100,default='Y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  #a1= Address(city='pune1',state='MH',pincode=4445411)

    class Meta:
        db_table='AddressInfo'

class Customer(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    balance=models.FloatField()
    email=models.EmailField(max_length=100,unique=True)
    active=models.CharField(max_length=100,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    adrref=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

   #c1=Customer(name='pragati',age=25,balance=567.890,email='pragati1.vtpl@gmail.com')
    class Meta:
        db_table='CustomerInfo'