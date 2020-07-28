from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from .forms import SearchInputForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'spider/index.html', {'form': SearchInputForm()})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            print(user)
            login(request, user)
            return redirect("homepage")
    if request.user.username == '':
        print("not login")
        form = UserCreationForm
        return render(request = request, template_name="registration/registration.html", context={"form": form})
    print("logged in")
    return redirect("homepage")

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