from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mentee-registration/', views.mentee, name='mentee'),
    path('mentor-registration/', views.mentor, name='mentor'),
]
