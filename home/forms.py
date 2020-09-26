from django import forms
from home.models import Project,Currency ,PRICE_TYPES,Replies



LEVEL_TYPES=((1, 'Entry Level'), (2, 'Intermediate'), (3, 'Expert'))


class ProjectForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    # description=forms.(widget=forms.TextInput(attrs={'placeholder': 'Long description'}))
    price_min=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Minimum price'}))
    price_max=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Maximum price'}))
    skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Skills'}))
    upload_files=forms.FileField(widget=forms.FileInput())
   


    class Meta:
        model=Project
        fields=['title','description','price_min','price_max','level','skills','upload_files','currency','price_type',]
        widgets = {
            'description':forms.Textarea(attrs={
                
                'placeholder': 'Description'
            }),
            'level':forms.RadioSelect(),
            'currency':forms.Select(attrs={
                'placeholder':'select'
            })
        }
class RepliesForm(forms.ModelForm):
    
    duration=forms.DateTimeField()
    
    class Meta:
        model=Replies
        fields=['reply','duration']
        