from django.contrib import admin

from flashcards.models import *

admin.site.register(Flashcard)
admin.site.register(Review)