from django import forms
from home.models import Project



class ProjectForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    short_description=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Short description'}))

    # long_description=forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Long description'}))
    # price_type=forms.ChoiceField(widget=forms.ChoiceField())
    price_min=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Minimum price'}))
    price_max=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Maximum price'}))
    level=forms.ChoiceField(widget=forms.RadioSelect())
    skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Skills'}))
    upload_files=forms.FileField(widget=forms.FileInput())



    class Meta:
        model=Project
        fields=['title','short_description','long_description','price_min','price_max','level','skills','upload_files']
        widgets = {
            'long_description':forms.Textarea(attrs={
                
                'placeholder': 'Long description'
            }),
        }
