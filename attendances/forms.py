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

class QuizForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'classroom', 'question1',
                'question2', 'question3',
                'question4', 'question5')
        model = models.Quiz

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nama'})
        self.fields['classroom'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Kelas'})
        self.fields['question1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tuliskan ayat tersebut'})
        self.fields['question2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tuliskan jawabanmu'})
        self.fields['question3'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tuliskan jawabanmu'})
        self.fields['question4'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tuliskan jawabanmu'})
        self.fields['question5'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tuliskan jawabanmu'})
