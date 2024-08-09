from django.db import models
from django.utils import timezone
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




