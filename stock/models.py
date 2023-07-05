from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField()
    purchased = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name
