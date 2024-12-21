from django.urls import path

from . import views

app_name = 'math'

urlpatterns = [
    path('', views.mathematics, name='mathematics'),
    path('realisation/', views.realisation, name='realisation'),
]

