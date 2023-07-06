from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm


def store(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
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
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def account(request):
    return render(request, 'store/account.html')


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