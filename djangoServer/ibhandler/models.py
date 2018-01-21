from django.db import models

# Create your models here.

class Ticket(models.Model):
    ask_price = models.FloatField(default=0)
    bit_size = models.FloatField(default=0)
    last_size = models.FloatField(default=0)
    bid_price = models.FloatField(default=0)
    close_price = models.FloatField(default=0)



