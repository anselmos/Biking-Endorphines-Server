"""
Models for API - an empty one for now.
Contains only a receiver for making tokens for new-users on a post_save method.
"""
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
# pylint: disable=unused-argument
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Makes Token for newly created users
    """
    if created:
        Token.objects.create(user=instance)
