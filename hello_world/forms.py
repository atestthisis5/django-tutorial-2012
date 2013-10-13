from django.forms import ModelForm
from hello_world import models

class EventsForm(ModelForm):
    class Meta:
        model=models.Events