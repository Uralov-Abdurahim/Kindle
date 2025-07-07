from django.db import models

class Overview(models.Model):
    icon = models.ImageField(upload_to='Overview/%Y/%m/%d')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Overview'
        verbose_name_plural = 'Overviews'