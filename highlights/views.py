from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, HighlightsSqliteForm

# from .file_processor import handle_uploaded_file

def upload_file(request):
    if request.method == "POST":
        form = HighlightsSqliteForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALID")
            # handle_uploaded_file(request.FILES["file"])
            form.save()
            return HttpResponseRedirect("/flashcards/")
        print("NOT VALID")
    else:
        print("NOT NOT VALID")
        form = HighlightsSqliteForm()
    return render(request, "highlights/upload.html", {"form": form})


def handle_uploaded_file(f):
    with open("blob", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)