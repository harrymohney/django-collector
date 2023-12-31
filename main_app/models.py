from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  size = models.TextField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})