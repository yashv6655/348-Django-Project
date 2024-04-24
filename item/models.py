from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Item(models.Model):
    def __str__(self):
        return self.name
    type = models.ForeignKey(Type, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    posted_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)