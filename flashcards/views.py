from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Flashcard
from django.template import loader

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