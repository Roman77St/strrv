from django.contrib import admin

from .models import Recomendation


@admin.register(Recomendation)
class AdminRecomendation(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


