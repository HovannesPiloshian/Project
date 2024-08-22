from django.contrib import admin
from .models import Logo, Slide, Category, Product, Tag
# Register your models here.
admin.site.register(Logo)
admin.site.register(Slide)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)