from .models import News  
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsSerializer


class makeNewNews(CreateAPIView):
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsSerializer
    
    
class publishedNews(ListAPIView):
    queryset = News.objects.filter(status='P')
    serializer_class = NewsSerializer