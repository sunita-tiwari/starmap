from django.db import models
import uuid

class Product(models.Model):
    """
    This model save the product data.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    location = models.CharField(max_length=555, help_text='location of the product')
    date = models.CharField(max_length=255, help_text='date of the product')
    star_color = models.CharField(max_length=100, help_text='star color of the product')
    frame_color = models.CharField(help_text='frame color of the product', max_length=100)
    bg_color = models.CharField(help_text='Background color of the product', max_length=100)
    text_color = models.CharField(help_text='text color of the product', max_length=100)
    constellations = models.BooleanField(default=False)
    grid = models.BooleanField(default=False)
    message = models.TextField()
    lat = models.CharField(help_text='Lattitude of the product', max_length=255)
    lng = models.CharField(help_text='Longitude of the product', max_length=255)
    font = models.CharField(max_length=100, help_text="text font")
    svg_image = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.date


