from django.urls import path
from . import views


app_name = 'watcher'

urlpatterns = [
    path('update/', views.update_product_price, name='update'),
    path('list/', views.current_product_under_watch, name='list'),
    path('add/', views.create_watching_product, name='add'),
    path('list/edit/<int:pk>/', views.edit_under_watch_product, name="edit"),
    path('list/delete/<int:pk>/', views.delete_under_watch_product, name='delete'),
]