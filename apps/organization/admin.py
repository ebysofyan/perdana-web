from django.contrib import admin

from .models import Club, Member

# Register your models here.

admin.site.register(Member)
admin.site.register(Club)
