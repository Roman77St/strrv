from django.urls import path

from . import views

app_name = 'mathematics'

urlpatterns = [
    path('', views.mathematics, name='mathematics'),
]

