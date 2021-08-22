from django.db import models
import uuid


class TimeStamp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    time_stamp = models.DateTimeField(auto_now=True)

    create_time = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
