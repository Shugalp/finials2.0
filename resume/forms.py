from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Letter

class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = (
            "name",
            "email",
            "subject",
            "message",
            )
        
