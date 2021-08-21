from django.urls import path
from resume.views import Home,Contact,Resume

# app_name = 'post'

urlpatterns = [
    path('',Home,name="home"),
    path('contact/',Contact,name="contact"),
    path('resume/',Resume,name="resume"),

]