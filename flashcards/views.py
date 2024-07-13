from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Flashcard

def index(request):
    """ flashcards = Flashcard.objects.all()
    template = loader.get_template("flashcards/index.html")
    context = {
        "flashcards": flashcards
    }
    return HttpResponse(template.render(context, request)) """

    flashcards = Flashcard.objects.all()
    context = {"flashcards": flashcards}
    return render(request, "flashcards/index.html", context)


def detail(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_id)
    return render(request, "flashcards/detail.html", {"flashcard": flashcard})

def add(request):
    try:
        front = request.POST["front"]
        back = request.POST["back"]
    except (KeyError):
        return render(
            request,
            "flashcards/index.html",
            {
                "error_message": "You need to provide a front and back for the flashcard",
            },
        )
    except:
        return render(
            request,
            "flashcards/index.html",
            {
                "error_message": "An error occurred",
            },
        )
    else:
        f = Flashcard(front=front, back=back)
        f.save()
        HttpResponseRedirect(reverse("flashcards:detail", args=(f.id,)))