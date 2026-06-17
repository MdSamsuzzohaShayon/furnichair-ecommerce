from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    preview = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name