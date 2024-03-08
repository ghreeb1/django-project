from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("welcome mr/ghareeb")
def second(request):
  return HttpResponse("<h1>welcome mr/ahmed</h1> ")