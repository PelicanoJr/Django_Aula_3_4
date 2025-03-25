from django import forms
from filmes.models import Genero

class FilmeForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    sinopse = forms.CharField(widget=forms.Textarea)
    duracao = forms.IntegerField()
    ano = forms.IntegerField()
    genero = forms.ModelChoiceField(Genero.objects.all())
    diretor = forms.CharField(max_length=100)  
    atores = forms.CharField(max_length=100)
    poster = forms.ImageField()

