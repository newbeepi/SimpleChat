from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


def validate_num_participants(value):
    if len(value) > 2:
        raise ValidationError("Thread can have maximum 2 participants")


class Thread(models.Model):
    participants = models.ManyToManyField(User, related_name="threads", validators=[validate_num_participants])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_participants(self):
        return [participant.username for participant in self.participants.all()]


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
