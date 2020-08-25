from django.db import models


class Latest_option(models.Model):

    name = models.CharField(max_length=254)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    antiquity_id = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name
