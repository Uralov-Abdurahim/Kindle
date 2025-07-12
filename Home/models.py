from django.db import models

class Home(models.Model):
    image = models.ImageField(upload_to='Home/%Y/%m/%d')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=255)
    file = models.FileField(upload_to='Home/%Y/%m/%d')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'