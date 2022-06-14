from functools import partial
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models  import Book
from .serializer import BookSerializer
from rest_framework import status

from BookApi import serializer

from rest_framework import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Our GET Api is working fine'
        })
    if request.method == 'POST':
         return Response({
            'status': 200,
            'message': 'Our POST Api is working fine'
        })


@api_view(['GET'])
def get_all_books(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    #return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book)
    #return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def createBook(request):
    book_item = BookSerializer(data=request.data)

    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Data already existing!')
    try:
        if book_item.is_valid():
            book_item.save()
            return Response(book_item.data, status=status.HTTP_201_CREATED)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateBook(request, id):
    item = Book.objects.get(pk=id)

    reqdata = BookSerializer(item, data=request.data, partial=True)

    if reqdata.is_valid():
        reqdata.save()
        return Response(reqdata.data,  status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)    
    
