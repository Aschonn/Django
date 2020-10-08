#forms import
from django import forms

#models import
from django.contrib.auth.models import User
from .models import Year, Player


class SubmitMock(forms.Form):
    
    mock = forms.ModelChoiceField(queryset=Year.objects.all(), empty_label=None)

    class Meta:
        #Which model/table do we want to toggle/use
        model = Player
        #fields that will be shown
        fields = ['mock']
        ordering = ['year_rank']




    