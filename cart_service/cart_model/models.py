from django.db import models

# Create your models here.
class Cart(models.Model):
    
    product_id = models.CharField( max_length=50)
    username = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    product_size = models.CharField(max_length=2, default='36')
    count = models.CharField(max_length=5)
    totalprice = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.product_id, self.username, self.product_category, self.product_name, self.product_size, self.count, self.totalprice)
    class Meta:
        db_table = "cart"


