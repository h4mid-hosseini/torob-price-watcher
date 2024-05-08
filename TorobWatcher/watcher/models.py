from django.db import models


class WatchingProducts(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    notice_price = models.PositiveBigIntegerField()

    last_price = models.PositiveBigIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class WatchDogBark(models.Model):
    title = models.CharField(max_length=200)
    product = models.ForeignKey(WatchingProducts, on_delete=models.CASCADE, related_name='barks')
    price = models.PositiveBigIntegerField()
    action_taken = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)