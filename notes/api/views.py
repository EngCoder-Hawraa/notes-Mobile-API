from django.shortcuts import render
# Create your views here.
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from api import serializers




@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint':'/notes',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new note with data sent in post req'
        },
         {
            'Endpoint':'/notes/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in post req'
        },
          {
            'Endpoint':'/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes and existing note'
        },
    ]
    return Response(routes)


@api_view(['GEt'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GEt'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
