from django.db import models

class Testimonial(models.Model):
    sentences = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Testimonial/%Y/%m/%d')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'