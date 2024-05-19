from django.contrib import admin
from . import models


@admin.register(models.WatchingProducts)
class WatchProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_price', 'last_price', 'updated_at', 'created_at')
    list_editable = ('notice_price',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.WatchDogBark)
class WatchProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'updated_at', 'action_taken')
    list_editable = ('action_taken',)
    readonly_fields = ('created_at', 'updated_at')