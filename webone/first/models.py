from django.db import models

class TextInputForm(models.Model):
    text = models.TextField()

from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField()
