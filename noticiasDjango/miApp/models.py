from django.db import models

# Create your models here.
class Noticias(models.Model):
    tituloNoticia = models.CharField(max_length=75)
    descripcioCorta = models.CharField(max_length=100)
    descripcioLarga = models.CharField(max_length=1000)
    fechaNoticia = models.DateField()
    imagenNoticia = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.tituloNoticia
