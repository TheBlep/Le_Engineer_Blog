from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Django views used:


def about_me(request):
    """
    Renders the most recent information on the website author and allows
    user collaberation requests
    --from which model this veiw displays data:
    --list the two variables returnsed by the context in the veiw. and
    from where thy get the data
    -- state which template is returned by this view
    Displays an indevidual instant of :model:`about:About`.
    **context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration\
             request received! Ill try to respond within 2 working days.")
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
