from django import forms
from . import models


class ClubLeadForm(forms.Form):
    member_id = forms.CharField()


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
        exclude = ['lead', ]


class MemberForm(forms.ModelForm):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45)
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45, required=False)
    club_id = forms.CharField(max_length=5)

    class Meta:
        model = models.Member
        exclude = ['user', 'club', ]
