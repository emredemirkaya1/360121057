from django.contrib import admin

from .models import Portfolio, Teamss


@admin.register(Teamss)
class TeamssAdmin(admin.ModelAdmin):
    list_display = ('firstname',)
    list_filter = ('country',)
    search_fields = ('firstname',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ('name',)

