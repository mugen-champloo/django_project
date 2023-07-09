from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
import json





def store(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    user = request.user
    context = {'products': products, 'categories': categories, 'user': user}
    return render(request, 'store/store.html', context)

def all_product(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products': products, 'categories': categories}
    return render(request, 'store/all_product.html', context)

def watch(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    categories = Category.objects.all()
    images_for_watch = Images.objects.all()
    context = {'product': product, 'categories': categories, 'images_for_watch': images_for_watch}
    return render(request, 'store/watch.html', context=context)

def categories(request, cat_slug):
    cats = get_object_or_404(Category, slug=cat_slug)
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"cat": cats, 'products': products, 'categories': categories}
    return render(request, 'store/categories.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, compled=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def updateItem(request):   #связь между js
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, compled=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

def checkout(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, compled=False)
      items = order.orderitem_set.all()
   else:
      items = []
      order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
   
   context = {'items':items, 'order':order}
   return render(request, 'store/checkout.html', context)

def account(request):
    return render(request, 'store/account.html')

def profile(request):
    # user = User.objects.all()
    # context = {'user': user}
    return render(request, 'store/profile.html', {'user': request.user})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store') 
        else:
            # Добавьте ошибки формы в контекст представления
            errors = form.errors.as_data()
            return render(request, 'store/login.html', {'form': form, 'errors': errors})
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

class LoginView(LoginView):
    template_name = 'store/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('store')


class RegisterPage(FormView):
    template_name = 'store/register.html'
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('store')
        return super().get(*args, **kwargs)
    
# def create_customer(request):
#     customer = Customer.objects.get(user=request.user)


#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Действия после успешного сохранения формы
#             return render(request, 'store/store.html')
#     else:
#         form = CustomerForm()
#     return render(request, 'store/castomer.html', {'form': form})