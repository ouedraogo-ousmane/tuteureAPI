from django.contrib import admin
from .models import *

# Register your models here.

class AutoFilter(admin.ModelAdmin):
    list_display = ('id','name','path','language', 'numAnnotate','creation_date')
    list_filter = ('language',)

class AnnotationFilter(admin.ModelAdmin):
    list_display = ('id','emotion','audio','user','creation_date')


class EmotionFilter(admin.ModelAdmin):
    list_display =('id','name', 'emoji', 'creation_date')
    list_filter=('name',)

class AudioResultAnnotationFilter(admin.ModelAdmin):
    list_display=('id','audio', 'note_name', 'note_emoji' ,'creation_date')
    

admin.site.register(Audio, AutoFilter)
admin.site.register(Annotation, AnnotationFilter)
admin.site.register(Emotion, EmotionFilter)
admin.site.register(AudioResultAnnotation, AudioResultAnnotationFilter)