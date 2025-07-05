from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='Abot/%Y/%m/%d')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'