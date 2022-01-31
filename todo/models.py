"""Model creation file"""
from django.db import models

# Create your models here.

class Item(models.Model):
    '''
    A class to represent a todo item.
    Attributes
    ----------
    name : str max length 50.
        name of the item to be completed.
    done : boolean.
        indicator for completion of the item.
    '''
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)


    def __str__(self):
        ''' Override default to return item name instead of primary key.'''
        return self.name
