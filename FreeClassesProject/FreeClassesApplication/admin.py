from django.contrib import admin

# Register your models here.
from .models import DocumentData

class documentadmin(admin.ModelAdmin):
    list_display = ['subject','files']
admin.site.register(DocumentData,documentadmin)