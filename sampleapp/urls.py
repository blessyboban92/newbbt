from .import views
from django.urls import path

urlpatterns = [
    
    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('customer/',views.customerf,name='customerf'),
    path('register/',views.registerf,name='registerf'),
]