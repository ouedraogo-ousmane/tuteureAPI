from django.contrib import admin

from .models import User, Language

# Register your models here.

class UserFilter(admin.ModelAdmin):
    list_display = ('id','email','username', 'job','language')
    list_filter = ('language',)


admin.site.register(User,UserFilter)

admin.site.register(Language)