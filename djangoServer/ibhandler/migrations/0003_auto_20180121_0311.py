# Generated by Django 2.0 on 2018-01-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibhandler', '0002_auto_20180121_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ask_size',
        ),
        migrations.AddField(
            model_name='ticket',
            name='ask_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='bid_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='bit_size',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='close_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_size',
            field=models.FloatField(default=0),
        ),
    ]
