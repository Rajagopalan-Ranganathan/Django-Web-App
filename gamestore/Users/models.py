from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
import uuid

from common.constants import USER_CHOICES


"""
@Class_Name: USerProfile
@Params: user, website,picture,user_type,activation_token,apikey
"""

# Model to Store the user details
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = CloudinaryField('picture', blank=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, default='P')
    activation_token = models.CharField(max_length=36, blank=True)
    apikey = models.UUIDField( blank=True, default=uuid.uuid4)
    class Meta:
        db_table = "UserProfile"

    def __str__(self):
        return self.user.username
