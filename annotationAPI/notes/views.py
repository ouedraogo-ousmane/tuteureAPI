
from rest_framework import generics, permissions
from .models import *
from .serializers import *



class HomeAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Audio
        liste des audio annoter par l'utilisateur et non par l'utilisateur
    '''
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    paginator = None
list_create_AudioPIVIEW = HomeAPIView.as_view()

class RetUpdateDelHome(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Audio 
    '''
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_AudioView = RetUpdateDelHome.as_view()

class EmotionAPICview(generics.ListCreateAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    paginator = None

class RetUpdateDelEmotion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator = None

class CreateAudio(generics.CreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [permissions.IsAdminUser]
    


class AnnotationUserAPIView(generics.ListCreateAPIView):
    serializer_class = AnnotationAudioSerializer
    permission_classes = [permissions.IsAuthenticated]
    #paginator = None  #switch on the pagination
    
    def get_queryset(self):
        # Return the list of Audio according to the connected user and this language
        limit_Annotation_Num = 5
        user = self.request.user
        return Audio.objects.filter(language__language = user.language,
                                    numAnnotate__lte=limit_Annotation_Num)
    

from django.db.models import Count

class UpdateAnnotationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        audio_annotate = Audio.objects.get(id=self.request.data["audio"])
        
        response = super().patch(request, *args, **kwargs)
        
        # calcul et enregistrement de l'annotation maximal pour l'audio
        
        annotation_compte = Annotation.objects.filter(audio=audio_annotate).values(
            'emotion').order_by().annotate(emotion_count=Count('emotion')) # donne l'annotion maximal
        
        max_val = max(annotation_compte, key=lambda x:x['emotion_count'])
        emotion_max = Emotion.objects.get(id=max_val["emotion"])
        
        audioResult = AudioResultAnnotation.objects.filter(audio=audio_annotate)
        
        if len(audioResult)==0:
            final_audio_note = AudioResultAnnotation(
            audio=audio_annotate, audio_name='', note_name = emotion_max.name, note_emoji=emotion_max.emoji)
            
            final_audio_note.save()
        else:
            for audioResult in audioResult:
                audioResult.note_name = emotion_max.name
                audioResult.note_emoji = emotion_max.emoji
                audioResult.save()
            
        return response
class PostAnnotationAPIView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        audio_annotate = Audio.objects.get(id=self.request.data["audio"])
        if(audio_annotate is not None):
            audio_annotate.numAnnotate+= 1
            audio_annotate.save()
        response = super().create(request, *args, **kwargs)
        
        # calcul et enregistrement de l'annotation maximal pour l'audio
        
        annotation_compte = Annotation.objects.filter(audio=audio_annotate).values(
            'emotion').order_by().annotate(emotion_count=Count('emotion')) # donne l'annotion maximal
        max_val = max(annotation_compte, key=lambda x:x['emotion_count'])
        
        emotion_max = Emotion.objects.get(id=max_val["emotion"])
        
        audioResult = AudioResultAnnotation.objects.filter(audio=audio_annotate)
        
        if len(audioResult)==0:
            final_audio_note = AudioResultAnnotation(
            audio=audio_annotate, audio_name='', note_name = emotion_max.name, note_emoji=emotion_max.emoji)
            final_audio_note.save()
        else:
            for audioResult in audioResult:
                audioResult.note_name = emotion_max.name
                audioResult.note_emoji = emotion_max.emoji
                audioResult.save()

        return response
    
class HomeVideoAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Video
        liste des Video annoter par l'utilisateur et non par l'utilisateur
    '''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    paginator = None
list_create_VideoPIVIEW = HomeVideoAPIView.as_view()

class AnnotationVideoUserAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = AnnotationVideoSerializer
    permission_classes = [permissions.IsAuthenticated]
    paginator = None


class RetUpdateDelVIDEOHome(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Audio 
    '''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_VideoView = RetUpdateDelVIDEOHome.as_view()
