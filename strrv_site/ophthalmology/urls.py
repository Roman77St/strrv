from django.urls import path
from . import views

app_name = 'ophthalmology'

urlpatterns = [
    path('', views.recomend_list, name='recomend_list'),
    path('clinical_recomendation/<slug:recomend_slug>/', views.RecomendItemView.as_view(), name='recomend_item'),
]
