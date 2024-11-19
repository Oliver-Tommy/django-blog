from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here

def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration request
    Displays an individual instanc eof :model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """
    if request.method == "POST":
        print("received a POST request")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            # collaborate = collaborate_form.save(commit=False)
            # collaborate.author = request.user
            # collaborate.post = post
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received.'
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
