from django import forms

class InviteForm(forms.Form):
    title = forms.CharField(max_length=100)
    sender = forms.EmailField()