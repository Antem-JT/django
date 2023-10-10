from django.db import models

# Create your models here.

class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title