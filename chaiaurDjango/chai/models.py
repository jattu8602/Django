from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVarity(models.Model):
  CHAI_TYPE_CHOICE=[
    ('ML','MASALA'),
    ('SP','SOUP'),
    ('ST','STUFFED'),
    ('CR','CRISPY'),
    ('CO','COOKED'),
    ('OT','OTHER')
  ]
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
  description = models.TextField(default='')



  def __str__(self):
    return self.name


# One to many

class ChaiReview(models.Model):
  chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.user.username} review for {self.chai.name}'


# Many to many
class Store(models.Model):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=100 )
  chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

  def __str__(self):
    return self.name




# one to one

class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateField(default= timezone.now)
  valid_until = models.DateField()

  def __str__(self):
    return f'Certificate for {self.name.chai}'

































