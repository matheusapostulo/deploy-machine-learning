#from django.http import HttpResponse
from django.shortcuts import render

def Welcome(request):
    #return HttpResponse('<h1>Olá<h1>')
    return render(request,'index.html')

def User(request):
    username = request.GET['username']
    #print(username)
    return render(request, 'user.html', {'name':username})