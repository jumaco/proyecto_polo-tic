from django.db import models


# Modelo de Categoria
class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


# Modelo de Producto
class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productos/', blank=False)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Informacíon del producto')
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
