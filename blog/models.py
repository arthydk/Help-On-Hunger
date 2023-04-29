from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    email=models.EmailField(max_length=100, null=False, blank=False)
    phone=models.IntegerField(null=False, blank=False)
    comment=models.TextField(max_length=1000, null=False,blank=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table='contact'
        
class user(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    email=models.CharField(max_length=100,null=False,blank=False)
    pass1=models.CharField(max_length=100,null=False,blank=False)
    pass2=models.CharField(max_length=100,null=False,blank=False)
    class Meta:
        db_table='user'

class dform(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    mail=models.CharField(max_length=100,null=False,blank=False)
    phone=models.CharField(max_length=20,null=False,blank=False)
    dno=models.CharField(max_length=10,null=False,blank=False)
    street=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=100,null=False,blank=False)
    state=models.CharField(max_length=100,null=False,blank=False)
    pin=models.CharField(max_length=20,null=False,blank=False)
    food=models.CharField(max_length=100,null=False,blank=False)
    quantity=models.CharField(max_length=100,null=False,blank=False)
    food=models.CharField(max_length=100,null=False,blank=False)
    time=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table='donate'

class customer(models.Model):
    email=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.email
    class Meta:
        db_table='customer'

class amount(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    email=models.CharField(max_length=100,null=False,blank=False)
    amount=models.IntegerField(null=False,blank=False)
    class Meta:
        db_table='moneyfm'