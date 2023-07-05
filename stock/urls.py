from django.urls import path 
from . import views

urlpatterns = [
    path('',views.stock_available,name='stock'),
    path('add/<int:id>',views.Purchase,name='add'),
    path('sub/<int:id>',views.Sale,name='sub'),
]