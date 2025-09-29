from django.shortcuts import render
from notesapp.models import Note
from notesapp.serializers import NoteSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view('GET', 'POST')
def notes(request):
    '''
    This function will be responsible for getting all our notes in our database
    In the GET request, we're trying to serialize it so it comes out in JSON format
    In the POST request, we're trying to deserialize the object to get it saved in our database 
    '''

    if request.method == "GET":
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)