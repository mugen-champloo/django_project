from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('all_products/', views.all_product, name='all'),
    path('product/<slug:product_slug>', views.watch, name='watch'),
    path('category/<slug:cat_slug>', views.categories, name='cat'),
    path('register/', views.login_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='store'), name='logout'),
    path('update_item/', views.updateItem, name="update_item"),
    # path('create_customer/', views.create_customer, name='create_customer'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('login/register/', views.RegisterPage.as_view(), name="register"),
    path('account/', views.account, name="account"),
]