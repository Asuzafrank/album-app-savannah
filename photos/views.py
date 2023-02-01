from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from .models import Album,Photo


# Create your views here.
def home(request):
    users = User.objects.all()
    
    return render(request, 'photos/home.html', {'users': users})

def add(request):
    albums = Album.objects.all() 
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['album'] != 'none':
            album = Album.objects.get(id=data['album'])
        elif data['album_new'] != '':
            album, created = Album.objects.get_or_create(title=data['album_new'])
        else:
            album = None

        for image in images:
            photo = Photo.objects.create(
                album=album,
                description=data['description'],
                image=image,
            )

        return redirect('album')

    context = {'albums': albums}
    return render(request, 'photos/add.html', context)

def album(request):    
    album = request.GET.get('album')
    if album == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(album__title=album)
    albums = Album.objects.all()
    context = {'albums': albums, 'photos': photos}
    return render(request, 'photos/album.html', context)

def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

   
