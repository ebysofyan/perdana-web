from django.shortcuts import render
# Create your views here.
from django.views.generic import FormView, ListView, TemplateView

from .forms import ClubForm, MemberForm
from .models import Club, Member


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class ClubListView(ListView):
    model = Club
    queryset = Club.objects.all()
    template_name = 'organization/club_list.html'


class ClubAddFormView(FormView):
    form_class = ClubForm
    template_name = 'organization/club_add.html'


class MemberListView(ListView):
    model = Member
    queryset = Member.objects.all()
    context_object_name = 'members'
    template_name = 'organization/member_list.html'


class MemberAddFormView(FormView):
    form_class = MemberForm
    template_name = 'organization/member_add.html'
