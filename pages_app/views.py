from django.shortcuts import render

def index(request):
    return render(request, 'pages_app/index.html')