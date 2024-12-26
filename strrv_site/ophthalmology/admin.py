from django.contrib import admin

from .models import Recomendation, CRContent


@admin.register(Recomendation)
class RecomendationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

@admin.register(CRContent)
class CRContentAdmin(admin.ModelAdmin):
    pass
