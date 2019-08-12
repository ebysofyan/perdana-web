from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Club(TimeStampedModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    date_register = models.DateField()
    lead = models.OneToOneField('Member', on_delete=models.SET_NULL, null=True, related_name='leading_club')
    logo = models.ImageField(upload_to='logo/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'club'


class Member(TimeStampedModel):
    """
    Use card_number/registration_number as username
    Use first_name and last_name in model User as field of name
    """
    GENDER_CHOICES = (('pria', 'Pria'), ('wanita', 'Wanita'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    born_place = models.CharField(max_length=45, null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    address = models.TextField()
    body_height = models.CharField(max_length=25, null=True, blank=True, default="0")
    body_weight = models.CharField(max_length=25, null=True, blank=True, default="0")
    draw_length = models.CharField(max_length=25, null=True, blank=True, default="0")
    # lead = models.BooleanField(default=False, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, related_name='member_set')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'member'
        ordering = ['created']
