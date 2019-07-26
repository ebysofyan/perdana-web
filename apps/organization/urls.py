from django.urls import path
from . import views

urlpatterns = [
    path('members', views.MemberListView.as_view(), name='members'),
    path('members/add', views.MemberAddFormView.as_view(), name='member_add'),
    path('clubs', views.ClubListView.as_view(), name='clubs'),
    path('clubs/add', views.ClubAddFormView.as_view(), name='club_add'),
]
