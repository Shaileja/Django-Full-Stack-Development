from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    picture=models.ImageField(upload_to='profile_pics', default = 'profile_pics/djangoguitar.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})


