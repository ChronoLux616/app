from django import forms


class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su nick o username',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
