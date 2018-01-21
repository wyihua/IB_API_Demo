from django.db import models

# Create your models here.

class Ticket(models.Model):
    ask_size = models.IntegerField(default=0)
    bit_size = models.IntegerField(default=0)
    last_size = models.IntegerField(default=0)
    bid_price = models.IntegerField(default=0)
    close_price = models.IntegerField(default=0)



