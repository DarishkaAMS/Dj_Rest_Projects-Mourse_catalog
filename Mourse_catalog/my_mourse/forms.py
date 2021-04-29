from django import forms

from .models import Mourse


class MourseForms(forms.ModelForm):
    class Meta:
        model = Mourse
        fields = ('title', 'author', 'description', 'q_lectures')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'q_lectures': forms.NumberInput(attrs={'class': 'form-control'}),
        }
