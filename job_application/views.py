from django.shortcuts import render


def index(request):
    # request is required to generate HttpResponse and make request data available in templates
    return render(request, "index.html")
