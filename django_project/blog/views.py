from django.shortcuts import render

posts = [
    {
        'author': 'AbeerGS',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et sint, eveniet magnam voluptas labore fugiat aliquam ex inventore in quaerat, explicabo, beatae sunt porro. Iste aspernatur quam sint ea quibusdam.',
        'date_posted': 'March 4, 2019'
    },
    {
        'author': 'Test User 1',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur, deleniti!',
        'date_posted': 'March 7, 2019'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
