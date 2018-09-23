from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
    def __str__(self):
        return '<News:id=' + str(self.id) + ', ' + self.title + '(' + str(self.url) + ')>'