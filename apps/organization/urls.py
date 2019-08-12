from django.urls import path

from . import views

urlpatterns = [
    path('members', views.MemberListView.as_view(), name='members'),
    path('member/add', views.MemberAddFormView.as_view(), name='member_add'),
    path('member/detail/<int:pk>', views.MemberDetailView.as_view(), name='member_detail'),
    path('member/edit/<int:pk>', views.MemberEditFormView.as_view(), name='member_edit'),
    path('member/delete/<int:pk>', views.MemberDeleteView.as_view(), name='member_delete'),
    path('clubs', views.ClubListView.as_view(), name='clubs'),
    path('club/add', views.ClubAddFormView.as_view(), name='club_add'),
    path('club/edit/<int:pk>', views.ClubEditFormView.as_view(), name='club_edit'),
    path('club/delete/<int:pk>', views.CLubDeleteView.as_view(), name='club_delete'),
    path('club/<int:pk>/lead', views.ClubLeadSelectFormView.as_view(), name='club_select_lead'),
]
