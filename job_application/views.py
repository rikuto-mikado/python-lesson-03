from django.shortcuts import render
from forms import ApplicationForm


def index(request):
    if request.method == "POST":
        form = ApplicationForm()
        first_name = request.POST.get("first_name")
    # request is required to generate HttpResponse and make request data available in templates
    return render(request, "index.html")
