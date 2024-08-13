from django.db import models

class DjangoProduct(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'