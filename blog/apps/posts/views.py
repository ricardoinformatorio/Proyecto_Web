from django.shortcuts import render
from .models import Posts
# Create your views here.



def posts(request):
    posts = Posts.objects.all()
    return render(request, 'post.html', {'posts' : posts})

#vistas basadas en funciones
