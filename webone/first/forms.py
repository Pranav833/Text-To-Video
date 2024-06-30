# forms.py
from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(label='Text', widget=forms.Textarea)

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label='PDF File')
