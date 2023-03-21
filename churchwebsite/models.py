from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='website/', blank=True, null=True)
    title = models.CharField(max_length=155)
    content = models.TextField()
    
    def __str__(self):
        return self.title
