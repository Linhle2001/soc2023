from django.db import models

# Create your models here.
class Order(models.Model):
    user_id = models.CharField(max_length=50)
    ship_id = models.CharField(max_length=50)
    product_id = models.CharField( max_length=50)
    product_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.user_id, self.ship_id, self.product_id, self.product_name,self.quantity, self.price)
    class Meta:
        db_table="order"


