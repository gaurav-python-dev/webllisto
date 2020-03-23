from django.db import models
from django.urls import reverse
#create your model here
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.SET_NULL)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={'pk': self.pk})
    def __str__(self):
        return self.product_name

