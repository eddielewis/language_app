from django import forms
from .models import HighlightsSqlite

class UploadFileForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    file = forms.FileField()



class HighlightsSqliteForm(forms.ModelForm):
    class Meta:
        model = HighlightsSqlite
        fields = ('document',)