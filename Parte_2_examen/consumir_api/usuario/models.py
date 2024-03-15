from django.db import models

# Create your models here.
class log(models.Model):
    url = models.CharField(max_length=200)
    status_code = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=True)