from django.db import models

class DjangoCustomer(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'