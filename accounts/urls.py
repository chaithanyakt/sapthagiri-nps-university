from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('attendance/', views.attendance, name='attendance'),
    path('fees/', views.fees, name='fees'),
    path('reports/', views.reports, name='reports'),
    path('placements/', views.placements, name='placements'),
]