from django.db import models

class BookCategory(models.Model):
    pass
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return super().name
    
from django.db import models

class Book(models.Model):
    tittle=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publishing_date=models.DateField()
    category=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    distribution_expense=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return super().tittle
# Create your models here.
