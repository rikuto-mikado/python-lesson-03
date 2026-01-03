from django.shortcuts import render

# The dot (.) is a relative import - it means "import from the same package/directory as this file"
from .forms import ApplicationForm
from .models import Form

# Django's messaging framework - displays temporary notifications to users (success, error, warning, etc.)
from django.contrib import messages

# EmailMessage class for sending emails with optional attachments and custom headers
from django.core.mail import EmailMessage


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

            # Left side = database field name (from model), Right side = variable holding the value
            # For example: first_name=first_name means "set the 'first_name' field to the value in the 'first_name' variable"
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = (
                f"A new job application was submitted, thank you {first_name}"
            )
            email_message = EmailMessage(
                "Form submission confirmation", message_body, to=[email]
            )
            email_message.send()

            messages.success(request, "Application submitted successfully!")
    # request is required to generate HttpResponse and make request data available in templates
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
