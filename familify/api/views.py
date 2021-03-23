from django.http import Http404
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.decoders import translate2Human, translate2Morse
from .serializers import TextSerializer


# Create your views here.

class ToTextViewSet(viewsets.ViewSet):
    """
    API ViewSet that supports retrieving conversion from Morse to text
    """
    serializer_class = TextSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        """
        Retrieve morse for a text encoded data
        :param: request:
        :return: object with morse tranlation
        """
        # get text parameter from request
        #text = request.data.dict()
        text = request.data.dict()
        print(text)
        try:
            morse_mesagge = translate2Human(text['text'])
            print(morse_mesagge)
        except:
            raise Http404
        serializer = TextSerializer(morse_mesagge)
        print(serializer)
        result = Response(serializer.data)
        # including content-type to the headers
        result['Content-Type'] = 'application/json'
        return result


class ToMorseViewSet(viewsets.ViewSet):
    """
    API ViewSet that supports retrieving conversion from text to Morse
    """
    serializer_class = TextSerializer
    permission_classes = (IsAuthenticated,)


    def create(self, request):
        """
        Retrieve morse for a text encoded data
        :param: request:
        :return: object with morse tranlation
        """
        # get text parameter from request
        text = request.data.dict()
        print(text)
        try:
            morse_mesagge = translate2Morse(text['text'])
        except:
            raise Http404
        serializer = TextSerializer(morse_mesagge)
        print(serializer)
        result = Response(serializer.data)
        # including content-type to the headers
        result['Content-Type'] = 'application/json'
        return result


class BitToMorse(viewsets.ViewSet):
    pass
