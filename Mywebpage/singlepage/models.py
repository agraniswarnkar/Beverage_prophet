from django.db import models

class AAPL(models.Model):
    date = models.DateTimeField(max_length=255)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    dividends = models.FloatField()

class META(models.Model):
    date = models.DateTimeField(max_length=255)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    dividends = models.FloatField()

class AMZN(models.Model):
    date = models.DateTimeField(max_length=255)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    dividends = models.FloatField()

class GOOGL(models.Model):
    date = models.DateTimeField(max_length=255)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    dividends = models.FloatField()
