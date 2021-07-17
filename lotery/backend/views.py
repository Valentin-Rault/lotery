from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from random import randint

from .models import Words
from .serializers import WordsSerializer

# Create your views here.
class RandomWord(APIView):
    def get(self, request, format=None):
        length = Words.objects.count()
        if length:
            random_word = Words.objects.all()[randint(0, length - 1)]
            word = WordsSerializer(random_word).data
            return Response(word, status=status.HTTP_200_OK)
        return Response({'message': 'No word found'}, status=status.HTTP_404_NOT_FOUND)
