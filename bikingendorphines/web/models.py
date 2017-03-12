"""
Models for web application
"""
from __future__ import unicode_literals

# disabling because this import will be used in future
# pylint: disable=unused-import
from django.db import models

class User(models.Model):
    """
    User model for obtaining personal information about biking riders
    """
    name = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __unicode__(self):
        """
        Returns User information when using str/printing
        """
        return self.name

    def bmi(self):
        """
        Body Mass Index calculator simplified to number
        """
        return (self.weight / (self.height * self.height)) * 10000
