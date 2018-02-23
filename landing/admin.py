from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    # сортиротвка в админке
    # list_filter = ['email']
    # поиск в админке
    search_fields = ['name', 'email']

    fields = ['email']

    class Meta:
        model = Client


# Register your models here.
admin.site.register(Client, ClientAdmin)
