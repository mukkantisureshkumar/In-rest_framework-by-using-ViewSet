from django.db import models

# Create your models here.
class Product_Category(models.Model):
    categoryname=models.CharField(max_length=100,primary_key=True)
    categoryid=models.PositiveIntegerField()
    def __str__(self):
        return self.categoryname

class Product(models.Model):
    categoryname=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
    def __str__(self):
        return self.pname
    