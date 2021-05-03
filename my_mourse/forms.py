from django import forms

from .models import Mourse


class MourseForm(forms.Form):
    class Meta:
        model = Mourse
        fields = ('title', 'content', 'image', 'end_date', 'q_lectures')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'q_lectures': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MourseModelForm(forms.ModelForm):
    class Meta:
        model = Mourse
        fields = ('title', 'slug', 'content', 'image', 'start_date', 'end_date', 'q_lectures')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'q_lectures': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Mourse.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
