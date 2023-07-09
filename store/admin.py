from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'image', 'company', 'cat', 'price')
    prepopulated_fields = {'slug': ('name',)}

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddres)

