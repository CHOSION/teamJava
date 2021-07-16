from django.contrib import admin

from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}



class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','slug','available_display','created','updated']
    list_filter = ['available_display','created','updated','category']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['available_display']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)