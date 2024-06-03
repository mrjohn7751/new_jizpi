from django import forms
from .models import ArticleElon, ArticleNews

class ArticleElonForm(forms.ModelForm):
    class Meta:
        model = ArticleElon
        fields = ['author', 'category', 'title', 'body', 'img']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ArticleNewsForm(forms.ModelForm):
    class Meta:
        model = ArticleNews
        fields = ['author', 'category', 'title', 'body', 'img']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }