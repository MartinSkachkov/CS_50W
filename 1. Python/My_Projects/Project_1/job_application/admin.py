from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    # променливата трябва да се казва точно list_display и параметрите трябва да съвпадат
    # точно с имената на Form данните
    list_display = ('first_name', 'last_name', 'email', 'resume')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_name',)
    readonly_fields = ('occupation', 'resume', 'email')
    
admin.site.register(Form, FormAdmin) # By registering a model, you make it accessible in the admin interface