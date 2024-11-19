from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here

def about_me(request):
    """
    Renders the About page
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
