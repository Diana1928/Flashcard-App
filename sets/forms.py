from django import forms
from .models import Set, Flashcard


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['category']


class CardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front', 'back']
