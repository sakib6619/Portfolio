from django.db import models

# Create your models here.
class userProfile(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    RELIGION = (
        ('Islam','Islam'),
        ('Hindu','Hindu'),
        ('Buddha','Buddha'),
        ('Mormonism ','Mormonism')
    )
    firstName = models.CharField(max_length=5)
    middleName = models.CharField(max_length=10, null=True, blank=True) # user wish blank or input
    lastName = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=16)
    phone = models.TextField(max_length=16)
    address = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=10)
    religion = models.CharField(choices=RELIGION, max_length=10)
    BirthDate = models.DateField()
    image = models.ImageField(upload_to='Profile_pc/')
