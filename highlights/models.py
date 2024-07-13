import uuid
from django.db import models

class Highlight(models.Model):
    def __str__(self):
        return self.text

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=240)

class HighlightsSqlite(models.Model):
    document = models.FileField(upload_to="user_uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)