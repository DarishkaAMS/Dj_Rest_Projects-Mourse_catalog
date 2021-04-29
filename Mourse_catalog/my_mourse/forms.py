from django import forms

from .models import Mourse


class MourseForm(forms.ModelForm):
    class Meta:
        model = Mourse
        fields = ('title', 'author', 'description', 'start_date', 'end_date', 'q_lectures')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How should we call it?'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What is it about?'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'q_lectures': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MourseEditForm(forms.ModelForm):
    class Meta:
        model = Mourse
        fields = ('title', 'description', 'start_date', 'end_date', 'q_lectures')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How should we call it?'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What is it about?'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'q_lectures': forms.NumberInput(attrs={'class': 'form-control'}),
        }
