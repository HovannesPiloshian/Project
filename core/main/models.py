from django.db import models

# Create your models here.
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text
    
class Slide(models.Model):
    background_image = models.ImageField(upload_to='slides/')
    headline = models.CharField(max_length=255)
    subheadline = models.CharField(max_length=255)
    button_text = models.CharField(max_length=50, default="Shop Now")
    button_link = models.URLField(default="#", blank= True)

    def __str__(self):
        return self.headline   

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name  

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name  

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name         