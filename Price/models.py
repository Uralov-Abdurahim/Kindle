from django.db import models

class Price(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    sub_title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'