from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2,"Title must be greater than 2 characters.")]
    )

    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='post_owner')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
