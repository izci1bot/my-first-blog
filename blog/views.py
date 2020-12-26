from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def post_list(request):
    return render(request, 'post_list.html', {})




