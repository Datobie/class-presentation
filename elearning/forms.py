from django import forms
from .model import formSection


class contactForm(forms.Form):
    class Meta:
        model = formSection
        fields = "__all__"

