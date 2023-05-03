from django.db import models
import shoes_model
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'category'
    def __str__(self):
        return '%s' % (self.name)
class Shoes(models.Model):
     ### The following are the fields of our table.
    product_id = models.CharField(max_length=10)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=50)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.product_id, self.product_category, self.product_name, self.availability, self.price, self.image)
    class Meta:
        db_table = 'shoes'
        managed = True
        verbose_name = 'shoes'

    