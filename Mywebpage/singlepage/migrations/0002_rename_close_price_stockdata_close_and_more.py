# Generated by Django 5.0.1 on 2024-02-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdata',
            old_name='close_price',
            new_name='close',
        ),
        migrations.RenameField(
            model_name='stockdata',
            old_name='open_price',
            new_name='open',
        ),
        migrations.RenameField(
            model_name='stockdata',
            old_name='ticker_symbol',
            new_name='ticker',
        ),
        migrations.AddField(
            model_name='stockdata',
            name='high',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='low',
            field=models.FloatField(default=0.0),
        ),
    ]
