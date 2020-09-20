from django import forms
from home.models import Project



class ProjectForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))

    class Meta:
        model=Project
        fields="__all__"
        
