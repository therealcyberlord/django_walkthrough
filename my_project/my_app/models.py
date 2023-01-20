from django.db import models

# Create your models here.
class Text(models.model):
    text = models.CharField(max_length = 100, null = True)
    time_sent = models.DateTimeField(auto_now_add= True)