from django.urls import path
from . import views

# URL patterns for the job application app
# Maps URL paths to their corresponding view functions

# Note: Do not include leading slashes in app-level URL patterns
# The root path "" matches the app's base URL (e.g., /job_application/)
# Other paths like "about" will be appended to the base URL (e.g., /job_application/about)
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
]
