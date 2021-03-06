from django.urls import  path
from . import views
 
urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/edit/<slug:meetup_slug>', views.edit_form, name='edit-form'),
    path('meetups/delete/<slug:meetup_slug>', views.delete, name='delete'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]