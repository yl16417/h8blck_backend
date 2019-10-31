from django.shortcuts import render
from rest_framework import generics
from .serializers import WordsSerializer
from .models import Word

# Create your views here.
from django.http import HttpResponse

class WordsRetrieveView(generics.ListAPIView):
    serializer_class = WordsSerializer

    def get_queryset(self):
        qs = Word.objects.all()
        return qs


