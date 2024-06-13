from django.db import models
from django.contrib.auth.models import User

class Manunited(models.Model):
      Name =models.CharField(max_length=80)
      Number=models.IntegerField()
      Age=models.IntegerField()
      country=models.CharField(max_length=80)
      image=models.ImageField(upload_to='images/', default='images/default.jpg')
      author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
      
      def __str__(self):
          return self.Name

    
