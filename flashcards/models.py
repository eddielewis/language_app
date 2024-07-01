from django.db import models

class Flashcard(models.Model):
    front = models.CharField(max_length=240)
    back = models.CharField(max_length=240)


class Review(models.Model):
    last_review = models.DateField()
    review_due = models.DateField()
    difficulty = models.IntegerField()
    flascard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)