from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginPage,name="login"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('store/', views.store, name="store"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),

]

