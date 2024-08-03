import uuid
from django.db import models
from django.contrib.auth.models import User

class Highlight(models.Model):
    def __str__(self):
        return self.text

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=240)
    # book_id = models.TextField()
    # book_alias = models.TextField()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class HighlightsSqlite(models.Model):
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)