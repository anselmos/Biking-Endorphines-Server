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
    surname = models.CharField(max_length=100, default="")
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

    def bmi_health_name(self, bmi):
        if bmi < 0:
            return None
        if bmi >= 0 and bmi <= 18.5:
            return "Underweight"
        if bmi > 18.5 and bmi <= 24.9:
            return "Normal weight"
        if bmi > 24.9 and bmi <= 29.9:
            return "Overweight"
        if bmi > 29.9:
            return "Obesity"


class Route(models.Model):
    """
    Route model. Defines Route by name, avg_route.
    """
    route_name = models.CharField(max_length=100)
    avg_route = models.FloatField(default=0.0)

    def __unicode__(self):
        "Returns Route name "
        return self.route_name


class UserRoute(models.Model):
    """
    User's routes
    """
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __unicode__(self):
        "Returns User id"
        return self.id_user


class Point(models.Model):
    """
    Points similar to gpx-data
    """
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    elevation = models.FloatField(default=0.0)

    def __unicode__(self):
        "Returns Point unicode"
        return str(self.lat) + "" + str(self.lon)


class RoutePoint(models.Model):
    """
    Route Points relations
    """
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_point = models.ForeignKey(Point, on_delete=models.CASCADE)

    def __unicode__(self):
        "Returns Route-Point relationship unicode"
        return self.id_route
