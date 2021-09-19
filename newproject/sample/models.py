from django.db import models
from django.contrib.auth.models  import AbstractUser 


# Create your models here.
class User(AbstractUser):
    usertype = models.CharField(max_length=50,default=True)
    age = models.IntegerField(verbose_name="Age",default=0)
    address = models.CharField(max_length=100,default=True)
    ph = models.IntegerField(default=0)
    city = models.CharField(max_length=50,default=True)
    pincode = models.IntegerField(default=0)

class Booking(models.Model):
    # custumer_name = models.CharField(max_length=50)
    # contact_number = models.IntegerField()
    # email = models.EmailField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)
    capacity = models.IntegerField()
    pickup_date = models.DateField(default="1999-12-14")
    dropoff_date = models.DateField(default="1999-12-14")
    pickup_address = models.CharField(max_length=100)
    dropoff_address = models.CharField(max_length=100)
    total_days = models.IntegerField(default=0)
    rate_perday = models.IntegerField(default=0)
    rate = models.IntegerField()

class CarBooking(models.Model):
    # custumer_name = models.CharField(max_length=50)
    # contact_number = models.IntegerField()
    # email = models.EmailField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)
    pickup_date = models.DateField(default="1999-12-14")
    dropoff_date = models.DateField(default="1999-12-14")
    pickup_address = models.CharField(max_length=100)
    dropoff_address = models.CharField(max_length=100)
    total_days = models.IntegerField(default=0)
    rate_perday = models.IntegerField(default=0)
    rate = models.IntegerField()


class BookingReports(models.Model):
    # custumer_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    # contact_number = models.IntegerField()
    Booking_Id =models.ForeignKey(Booking,on_delete=models.CASCADE)
    booking_date = models.DateField(default="1999-12-14")
    # capacity = models.IntegerField()
    # rate = models.IntegerField()

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    rate = models.IntegerField()
    image = models.FileField(upload_to='cars',max_length=300)


class Carimages(models.Model):
    image = models.FileField(upload_to='carimages',max_length=300)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ph = models.IntegerField()
    message = models.TextField()

class Addcar(models.Model):
    car_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    description = models.TextField(max_length=100)
    capacity = models.IntegerField()
    rate = models.IntegerField()

class Offers(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    image = models.FileField(upload_to='offers',max_length=300)
    actual_price = models.BigIntegerField()
    offer= models.BigIntegerField()

class OfferBooking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)
    pickup_date = models.DateField(default="1999-12-14")
    dropoff_date = models.DateField(default="1999-12-14")
    pickup_address = models.CharField(max_length=100)
    dropoff_address = models.CharField(max_length=100)
    offers=models.ForeignKey(Offers,on_delete=models.CASCADE)



class Images(models.Model):
     image = models.FileField(upload_to='car',max_length=300)
     title = models.CharField(max_length=200)
     stock = models.IntegerField(default=2)














    
    



