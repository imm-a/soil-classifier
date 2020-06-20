from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .process import munsell,displayMunsell, avgclr
from PIL import Image
# Create your views here.

def upload(request):
    context={}
    if request.method == 'POST' and request.FILES['myfile']:
        myfile =request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name,myfile)
        name = fs.save(myfile.name,myfile)
        url = fs.url(name)
        
        img = Image.open('C:/Users/amrit/projects/media/'+name)
        pixels = list(img.getdata())
        m=munsell(pixels)
        context['ans1']= m
        context['ans2']= displayMunsell(m)
        context['ans3']=avgclr(pixels)
        context['im'] = 'C:/Users/amrit/projects/media/'+name
    return render(request, 'soil/upload.html', context)