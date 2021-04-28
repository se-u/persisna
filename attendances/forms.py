from django import forms
from . import models

class PresenceForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'classroom', 'summary')
        model = models.Presence

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nama'})
        self.fields['classroom'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Kelas'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ringkasan'})