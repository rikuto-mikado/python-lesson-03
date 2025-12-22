from django import forms


# ApplicationForm class definition
# This class inherits from Django's forms.Form base class
# It is used to create and validate an application form for user input
# Django forms provide built-in validation and rendering capabilities
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
