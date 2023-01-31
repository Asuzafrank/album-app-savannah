from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Album,Photo


# Create your views here.
def home(request):
    users = User.objects.all()
    
    return render(request, 'photos/home.html', {'users': users})

def add(request):
    return render(request, 'photos/add.html')

def album(request):
    albums = Album.objects.all()
    photos = Photo.objects.all()
    context = {'albums': albums, 'photos': photos}
    return render(request, 'photos/album.html', context)

def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})
    
