from django.db import models
from djmoney.models.fields import MoneyField

class Story(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency="USD",
        max_digits=4,
    )
    artwork = models.FileField(upload_to="artworks/", blank=True)
    audio_file = models.FileField(upload_to="audios/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Stories"
