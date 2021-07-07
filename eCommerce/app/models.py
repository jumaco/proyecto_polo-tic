from django.db import models
import os


# Modelo de Categoria
class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='Descripción')
    featured = models.BooleanField(default=False, verbose_name='Destacado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


# Modelo de Producto
class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='Nombre')
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = models.ImageField(upload_to='productos/', blank=False, verbose_name='Imagen')
    excerpt = models.TextField(max_length=200, verbose_name='Resumen')
    detail = models.TextField(max_length=1000, verbose_name='Informacíon del producto')
    price = models.FloatField(verbose_name='Precio')
    available = models.BooleanField(default=True, verbose_name='Disponible')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Product, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
