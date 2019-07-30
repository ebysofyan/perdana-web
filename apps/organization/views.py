from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic import FormView, ListView, TemplateView

from .forms import ClubForm, MemberForm, ClubLeadForm
from .models import Club, Member


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class ClubListView(ListView):
    model = Club
    queryset = Club.objects.all()
    context_object_name = 'clubs'
    template_name = 'organization/club_list.html'


class ClubAddFormView(FormView):
    form_class = ClubForm
    template_name = 'organization/club_add.html'
    success_url = 'organization:clubs'

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return self.get(self.request)


class ClubLeadSelectFormView(FormView):
    form_class = ClubLeadForm
    template_name = 'organization/select_lead.html'
    success_url = 'organization:clubs'

    def get_object(self, **kwargs):
        return get_object_or_404(Club, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(ClubLeadSelectFormView, self).get_context_data(**kwargs)
        context['object'] = self.get_object()
        context['members'] = Member.objects.filter(club=self.get_object())
        return context

    def form_valid(self, form, **kwargs):
        member = get_object_or_404(Member, pk=form.cleaned_data['member_id'])
        club = self.get_object()
        club.lead = member
        club.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return self.get(self.request)


class MemberListView(ListView):
    model = Member
    queryset = Member.objects.all()
    context_object_name = 'members'
    template_name = 'organization/member_list.html'


class MemberAddFormView(FormView):
    form_class = MemberForm
    template_name = 'organization/member_add.html'
    success_url = 'organization:members'

    def get_context_data(self, **kwargs):
        context = super(MemberAddFormView, self).get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()
        return context

    def form_valid(self, form):
        user_data = {
            'username':  form.cleaned_data.pop('username'),
            'password': form.cleaned_data.pop('password'),
            'first_name': form.cleaned_data.pop('first_name'),
            'last_name': form.cleaned_data.pop('last_name'),
            'email': form.cleaned_data.pop('email')
        }
        user = User.objects.create_user(**user_data)

        # try:
        #     lead = form.cleaned_data.pop('lead') == '1'
        # except KeyError:
        #     form.cleaned_data['lead'] = False

        club_id = form.cleaned_data.pop('club_id')
        club = get_object_or_404(Club, pk=club_id)

        Member.objects.create(user=user, club=club, **form.cleaned_data)
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return self.get(self.request)
