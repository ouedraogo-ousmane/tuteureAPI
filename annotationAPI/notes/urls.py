
from django.urls import path
from .views import *


urlpatterns = [
    path('emotion/list/', view=EmotionAPICview.as_view(), name="emotion"),
    
    #Audio
    path('audio/list/', view=list_create_AudioPIVIEW, name="audio"),
    path('audio/mark/', view=AnnotationUserAPIView.as_view(), name='list_audio'),
    path('audio/mark/<int:pk>/update/', view=AnnotationUserAPIView.as_view(), name='note_update'),
    path('audio/<int:pk>/detail/', view=ret_upate_del_AudioView, name="updateNoteaudio"),
    
    #Video 
    path('Video/list/', view=list_create_VideoPIVIEW, name="video"),
    path('video/mark/', view=AnnotationVideoUserAPIView.as_view(), name='list_video'),
    path('video/mark/<int:pk>/update/', view=AnnotationVideoUserAPIView.as_view(), name='video_update'),
    path('video/<int:pk>/detail/', view=ret_upate_del_VideoView, name="updateNotevideo"),
    
    #Perform Annotation des audios
    path('audio/post/', view=PostAnnotationAPIView.as_view(), name="PostNotevideo"),
    path('audio/<int:pk>/update/', view=UpdateAnnotationAPIView.as_view(), name="update_audio_note"),
    
]