from django.contrib import admin
from .models import *

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

admin.site.register(Grocery, GroceryAdmin)

