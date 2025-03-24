from django.db import models

# Create your models here.

class ModeratedText(models.Model):
    text = models.TextField()
    is_hateful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Hateful' if self.is_hateful else 'Safe'} - {self.text[:50]}"