from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='courses')
    price = models.FloatField()
    category = models.ForeignKey(Category,related_name='courses_category',on_delete=models.SET_NULL,null=True)
    
    
    def __str__(self):
        return self.name