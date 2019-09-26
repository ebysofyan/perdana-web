from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.organization import models as org_models

PIC_TYPE = (
    ('personal', 'Personal'),
    ('club', 'Club'),
    ('dpc', 'DPC'),
)
# Create your models here.


class ArcheryRange(TimeStampedModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    pic_type = models.CharField(max_length=25, choices=PIC_TYPE)
    pic_club = models.ForeignKey(org_models.Club, on_delete=models.SET_NULL, related_name='archery_range',
                                 null=True, blank=True)
    pic_personal = models.ForeignKey(org_models.Member, on_delete=models.SET_NULL, related_name='archery_range',
                                     null=True, blank=True)
    paid_status = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=50, default=0, blank=True, null=True, decimal_places=25)

    def __str__(self):
        return '%s in %s' % (self.name, self.address)

    class Meta:
        db_table = 'archery_range'
