from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})
    

class Cars(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Машина")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})
    

class Product(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    info = models.TextField(blank=True, verbose_name="Текст статьи")
    car = models.ForeignKey('Cars', on_delete=models.CASCADE, verbose_name='Машина')
    company = models.CharField(max_length=70)
    image = models.ImageField(null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField()



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('watch', kwargs={'product_slug': self.slug})
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Images(models.Model):
    name = models.ForeignKey('Product', on_delete=models.DO_NOTHING, verbose_name='Name')
    image = models.ImageField(null=True, blank=True)
 
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    compled = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddres(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.address