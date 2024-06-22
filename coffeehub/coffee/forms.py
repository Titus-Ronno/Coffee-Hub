# forms.py
from django import forms
from .models import Reply
from .models import TrainingSession
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'email', 'comment']

# Schedule training

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['user','date', 'time', 'duration', 'details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

