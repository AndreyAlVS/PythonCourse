import datetime
from django import forms


class GameForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('coin', 'монетка'), ('cube', 'кости'), ('number', 'число')])
    num_tries = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(max_length=1500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'type': 'date'}))
