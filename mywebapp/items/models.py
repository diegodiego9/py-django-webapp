from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Collection(models.Model):
    item = models.ForeignKey(Item, on_delete=None)
    name = models.CharField(max_length=200)
