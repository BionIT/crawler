from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from .forms import SearchInputForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'spider/index.html', {'form': SearchInputForm()})

@api_view(['POST'])
def createItem(request):
    if request.is_ajax() and request.method == 'POST':
        form = SearchInputForm(request.POST)
        if request.user.username == '':
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if form.is_valid():
            serializer = ItemSerializer(data={'source': request.POST.get('source'), 'userId': request.user.id})
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                form = SearchInputForm()
                return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def item(request, itemName):
    if request.method == 'GET':
        items = Item.objects.filter(name__contains=itemName)
        serializer = ItemSerializer(items, context={'request': request}, many=True)
        return Response(serializer.data)
    #create new item
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)