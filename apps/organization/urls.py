from django.urls import path
from . import views

urlpatterns = [
    path('members', views.MemberListView.as_view(), name='members'),
    path('member/add', views.MemberAddFormView.as_view(), name='member_add'),
    path('clubs', views.ClubListView.as_view(), name='clubs'),
    path('club/add', views.ClubAddFormView.as_view(), name='club_add'),
    path('club/<int:pk>/select', views.ClubLeadSelectFormView.as_view(), name='club_select_lead'),
]
