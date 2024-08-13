from django.db import models
from .customer import DjangoCustomer
from .product import DjangoProduct

class DjangoOrder(models.Model):
    STATUS_CHOICES = [
        ('RECEIVED', 'Recebido'),
        ('PENDING', 'Pendente de pagamento'),
        ('CONFIRMED', 'Confirmado'),
        ('PREPARING', 'Em Preparação'),
        ('READY', 'Pronto'),
        ('FINISHED', 'Finalizado'),
        ('CANCELED', 'Cancelado'),
    ]
    
    customer = models.ForeignKey(DjangoCustomer, on_delete=models.CASCADE)
    products = models.ManyToManyField(DjangoProduct)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='RECEIVED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'core'