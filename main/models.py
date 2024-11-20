import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User
from django.db import models

class SurvivalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    time = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    