from django import forms
from django.contrib.auth.models import User
from core.models import Profile, Task, TaskType
from datetime import date

class NewTaskForm(forms.ModelForm):
    profile = forms.ModelChoiceField(queryset=Profile.objects.all(), label='Created By', empty_label=None)
    task_type = forms.ModelChoiceField(queryset=TaskType.objects.all(), empty_label=None)
    datetime = forms.DateTimeField(help_text='Required. Format: YYYY-MM-DD HH:MM', input_formats=['%Y-%m-%d %H:%M'])
    duration = forms.DurationField(help_text='Required. In minutes')

    class Meta:
        model = Task
        fields = ('profile', 'task_type', 'datetime', 'duration')
