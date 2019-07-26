from django import forms
from . import models


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = '__all__'


class MemberForm(forms.ModelForm):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45)
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45, required=False)

    class Meta:
        model = models.Member
        exclude = ['user', ]
