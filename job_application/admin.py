from django.contrib import admin

# Import the Form model from the models module in the current package
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    # Sort entries by first_name in descending order (Z to A) - the minus sign indicates reverse ordering
    ordering = ("-first_name",)
    readonly_fields = ("occupation",)


admin.site.register(Form, FormAdmin)
