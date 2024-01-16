from django.db import models


class Juice(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="juices/", null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    juices = models.ManyToManyField(Juice)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
