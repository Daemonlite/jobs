from django.urls import path
from django.contrib.auth.views import LogoutView
from find.views import *
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('',jobs,name='jobs'),
    path('application/',Application.as_view(),name='application'),
    path('add-company/',add_company.as_view(),name='add-company'),
    path('individual/',individual,name='individual'),
    path('individual-form/',Individual_form.as_view(),name='individual-form'),
   
    # path('job-detail/<int:pk>/',job_detail.as_view(),name="job-detail"),
]