from django import forms

class Mensaje(forms.Form):
    user_prompt = forms.CharField(required=True, max_length=100)
    user_file = forms.FileField(required=True)
