from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateTimeField(auto_created=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
