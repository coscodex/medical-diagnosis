from django import forms
from .models import Symptom

class DiagnosisForm(forms.Form):
    symptom1 = forms.ModelChoiceField(queryset=Symptom.objects.all(), required=True)
    symptom2 = forms.ModelChoiceField(queryset=Symptom.objects.all(), required=True)
    symptom3 = forms.ModelChoiceField(queryset=Symptom.objects.all(), required=True)
    symptom4 = forms.ModelChoiceField(queryset=Symptom.objects.all(), required=True)
