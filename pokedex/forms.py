from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            'heigth': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'heigth'}),
            'weigth': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'weigth'}),
            'Trainer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Trainer'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
                                    
                                    
        }