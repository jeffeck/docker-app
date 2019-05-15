from django.shortcuts import render
from django.http import HttpResponse

# Testing data 
# Get this from database, csv, etc.
posts = [
    {
        'author': 'Jeff',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'May 14, 2019'
    },
        {
        'author': 'John',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'May 14, 2019'
    }

]


# Create your views here.
def home(request):
    context = {
        'posts': posts 
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})




