from django import forms

class FileForm(forms.Form):
    document = forms.FileField(label='Upload your documents', required=True)
    