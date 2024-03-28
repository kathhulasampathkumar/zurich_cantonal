from django.db import models

# Create your models here.

class user_master(models.Model):            
    username   =  models.CharField(max_length=50,null=True)
    contact =    models.CharField(max_length=20,null=True)
    email   =  models.CharField(max_length=50,unique=True)
    city    =   models.CharField(max_length=20,null=True)
    password    =   models.CharField(max_length=50,null=True)
    balance     = models.DecimalField(max_digits=25, decimal_places=10, null=True)
    USER_CHOICES = ( ('user', 'User'),('admin', 'Admin'),('other', 'Other'),    )
    user_type   = models.CharField(max_length=25, default='user', choices=USER_CHOICES)
    # user_type   = models.CharField(max_length=25,default="user")  # admin or user
    createdby   =  models.IntegerField(default=99) 
    delete1 =    models.IntegerField(default=0) 
    status =    models.IntegerField(default=1) 
    class Meta:
        db_table="user_master"

    
    
    
    
