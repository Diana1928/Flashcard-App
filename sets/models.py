from django.db import models


class Set(models.Model):
    category = models.CharField(max_length=128, blank=False, null=False, default=' ')

    def __str__(self):
        return self.category


class Flashcard(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)

    def __str__(self):
        return "(" + self.front + ", " + self.back + ")"
