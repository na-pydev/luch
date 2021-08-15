from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    manfacturer = models.CharField(max_length=255)
    model_name = models.CharField(max_length=250)
    country = models.CharField(max_length=255)
    description = models.TextField()
    image_link1 = models.CharField(max_length=255, blank=True)
    image_link2 = models.CharField(max_length=255, blank=True)
    image_link3 = models.CharField(max_length=255, blank=True)
    image_link4 = models.CharField(max_length=255, blank=True)
    special_product = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    color = models.CharField(max_length=255)
    category = models.ForeignKey("Category", verbose_name="Category", on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['added_date']

    def __str__(self) -> str:
        return self.name


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image_link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['date']
