from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.checked:
            return self.title + " ✅"
        return self.title + " 🅾️"