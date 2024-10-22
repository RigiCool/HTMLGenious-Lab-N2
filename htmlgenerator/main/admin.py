"""Model registration in admin panel."""

from django.contrib import admin
from . models import Page, Slide

admin.site.register(Page)
admin.site.register(Slide)
