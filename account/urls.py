
from django.urls import path
from . import views


urlpatterns = [

    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('cancel',views.cancel,name='cancel'),
    path('logout',views.logout,name='logout')



]
