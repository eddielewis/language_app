from django.db import models

class Flashcard(models.Model):
    def __str__(self):
        return "\"" + self.front + "\"/\"" + self.back +  "\""

    front = models.CharField(max_length=240)
    back = models.CharField(max_length=240)


class Review(models.Model):
    def __str__(self):
        return str(self.difficulty) + " - " + str(self.review_due) + " - " + str(self.flashcard)
    
    last_review = models.DateField()
    review_due = models.DateField()
    difficulty = models.IntegerField()
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)