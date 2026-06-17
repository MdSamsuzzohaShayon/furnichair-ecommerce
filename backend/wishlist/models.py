from django.db import models

# Create your models here.
class Wishlist(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    preview = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email

