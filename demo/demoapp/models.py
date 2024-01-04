from django.db import models

# Create your models here.
class place(models.Model):
    place=models.CharField(max_length=250)
    desc=models.TextField()
    image=models.ImageField(upload_to='place')
    
    def __str__(self):
        return self.place