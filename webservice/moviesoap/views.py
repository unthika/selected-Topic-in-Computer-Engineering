from django.shortcuts import redirect, render
from django.http import HttpResponse
import sys
from SOAPpy import SOAPProxy
from SOAPpy import WSDL
import xml.etree.ElementTree as ET
serverUrl='http://localhost:8081'
namespace='xml'
server = SOAPProxy(serverUrl, namespace)

def home(request):
    return render(request, 'home.html')

def search_type(request):
    if request.method == 'POST' and request.POST.get('search','') == 'search':
        type_serch = request.POST['type']
        if(type_serch == ''):
            return redirect('/search/')
        return redirect('/show/%s/' %type_serch)
    return render(request, 'search.html')

def show_movie(request,type):
    response = server.movieNameFromeType(type)
    return render(request, 'show_movie.html',{'movie':response})

def add(request):
    if request.method == 'POST' and request.POST.get('send','') == 'send':
        movie_name = request.POST['movie_name']
        type_name = request.POST['type_']
        ac_names_list = request.POST['ac_names']
        director= request.POST['director']
        date = request.POST['date']
        mount = request.POST['mount']
        year = request.POST['year']
        type_ = type_name.split(',')
        ac_names = ac_names_list .split(',')
        server.update_xml(movie_name,type_,ac_names,director,date,mount,year)
    return render(request, 'add_movie.html')
