from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length = 200)
    sku         = models.CharField(max_length = 30)
    cost        = models.FloatField()
    price       = models.FloatField()
    stock       = models.IntegerField()

    def discount_price(self, discount):
        new_price = 0

        if discount > 0:
            discount = discount / 100
            new_price = self.price - (self.price * discount)

        return new_price

class KitProducts(models.Model):
    sku         = models.CharField(max_length = 30)
    quantity    = models.IntegerField()
    discount    = models.FloatField()

class Kit(models.Model):
    kit_name        = models.CharField(max_length = 200)
    kit_sku         = models.CharField(max_length = 30)
    products        = models.ManyToManyField(KitProducts)
