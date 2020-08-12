from django.forms import ModelForm
from .models import *

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
