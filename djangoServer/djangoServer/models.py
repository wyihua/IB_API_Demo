from django.db import models

class Ticket(models.Model):
    ask_size = models.IntegerField
    bit_size = models.IntegerField
    last_size = models.IntegerField
    bid_price = models.IntegerField
    close_price = models.IntegerField


