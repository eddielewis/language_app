from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm, HighlightsSqliteForm

# from .file_processor import handle_uploaded_file
@login_required
def upload_file(request):
    if request.method == "POST":
        form = HighlightsSqliteForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect("/flashcards/")
    else:
        form = HighlightsSqliteForm()
    return render(request, "highlights/upload.html", {"form": form})

def handle_uploaded_file(f):
    with open("blob", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)