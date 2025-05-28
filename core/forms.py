from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre completo'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'tuemail@example.com'})
    )
    telefono = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Tu numero de telefono (Opcional)'})
    )
    asunto = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder':'Escribe tu mensaje aqui....'})
    )
    mensaje = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...', 'rows': 6})
    )