from django.urls import path
from . import views


app_name = 'watcher'

urlpatterns = [
    path('update/', views.update_product_price, name='update')
]