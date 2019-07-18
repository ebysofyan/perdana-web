from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class Member(TimeStampedModel):
    """
    Use card_number/registration_number as username
    Use first_name and last_name in model User as field of name
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True)
    qrcode = models.ImageField(upload_to='qrcode/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'member'
        ordering = ['created']
