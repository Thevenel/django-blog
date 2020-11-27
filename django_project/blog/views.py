from django.shortcuts import render

posts = [
    {
        'author': 'Thevenel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 26, 2020'
    },
     {
        'author': 'Terlly',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 27, 2020'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})