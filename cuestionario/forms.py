from django import forms

class Mensaje(forms.Form):
    user_prompt = forms.CharField(required=True, max_length=100)
    user_file = forms.FileField(required=True)



# ALmacenamiento de formularios con verificacion de que es del usuario (por id) y si es publico o privado y obviamente del propio formulario en formato json

class AlmacenamientoFormulario(forms.Form):
    user_id = forms.IntegerField(required=True)
    is_public = forms.BooleanField(required=False)
    user_form = forms.FileField(required=True)