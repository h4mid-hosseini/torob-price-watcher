from django import forms
from . import models



class WatchingProductsForm(forms.ModelForm):
    class Meta:
        model = models.WatchingProducts
        fields = ['title', 'url', 'notice_price', 'email_address']
        