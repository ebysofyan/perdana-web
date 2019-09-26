from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.organization import models as org_models

# Create your models here.


class EquipmentCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default=None)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='childs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'equipment_category'


class Equipment(TimeStampedModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(EquipmentCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipments')
    owner = models.ForeignKey(org_models.Member, on_delete=models.SET_NULL, blank=True, null=True, related_name='equipments')
    approved = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='bow/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.owner.user.first_name, self.name)

    class Meta:
        db_table = 'equipment'
