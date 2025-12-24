from django.shortcuts import render
from forms import ApplicationForm


def index(request):
    if request.method == "POST":
        # Pass POST data to the form to bind submitted values for validation
        form = ApplicationForm(request.POST)
        # Check if the form data passes all validation rules
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            date = form.cleaned_data.get("date")
            occupation = form.cleaned_data.get("occupation")
    # request is required to generate HttpResponse and make request data available in templates
    return render(request, "index.html")
