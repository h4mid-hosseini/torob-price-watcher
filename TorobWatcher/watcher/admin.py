from django.contrib import admin
from . import models


@admin.register(models.WatchingProducts)
class WatchProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'notice_price', 'last_price', 'updated_at')
    list_editable = ('notice_price',)


@admin.register(models.WatchDogBark)
class WatchProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'updated_at')