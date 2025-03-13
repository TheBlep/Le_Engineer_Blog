from .models import CollaborateRequest
from django import forms

# Django models used:


class CollaborateForm(forms.ModelForm):
    """ A form for users to submit collaboration requests.
    model --from which model this form is created:
    feilds --list the fields included in the form and their purpose

    Creates a form based on the :model:`about.CollaborateRequest` model.
    **Fields:**
    ``name``
        The name of the user submitting the request.
    ``email``
        The email address of the user for contact purposes.
    ``message``
        The user's message or collaboration request details.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
