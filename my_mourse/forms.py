from django import forms

from .models import Mourse


class MourseForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class MourseModelForm(forms.ModelForm):
    class Meta:
        model = Mourse
        fields = ['title', 'slug', 'content', 'image', 'start_date', 'end_date', 'q_lectures']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Mourse.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
