# Generated by Django 5.0.1 on 2024-02-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0004_rename_close_price_stockdata_close_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AAPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=255)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('dividends', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AMZN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=255)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('dividends', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GOOGL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=255)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('dividends', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='META',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=255)),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('dividends', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
    ]
