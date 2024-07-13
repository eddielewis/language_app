from django.contrib import admin

from highlights.models import *

admin.site.register(Highlight)
admin.site.register(HighlightsSqlite)