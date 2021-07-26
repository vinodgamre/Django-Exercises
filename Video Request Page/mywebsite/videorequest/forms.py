from django import forms

class Videoform(forms.Form):
    videoname = forms.CharField(max_length=80,
    widget= forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Name',
    'id':'inputName'
    }))
    videodes = forms.CharField(widget= forms.Textarea(attrs ={
    'class':'form-control',
    'rows':'5',
    'id':'comment',
    'placeholder':'Name'
    }))
