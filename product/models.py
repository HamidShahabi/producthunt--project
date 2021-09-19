from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hunter')
    users = models.ManyToManyField(User, 'user')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
