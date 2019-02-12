from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50)
    contnet = models.CharField(max_length=100)
    last_update = models.DateField(auto_now_add = True)

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'page_id': self.id})
