from django import forms
from home.models import Project,Currency ,PRICE_TYPES,Replies
from django.forms import Form, ChoiceField
from inbox.models import Group
from django.contrib.admin import widgets                                       
from django.contrib.admin.widgets import AdminDateWidget

LEVEL_TYPES=((1, 'Entry Level'), (2, 'Intermediate'), (3, 'Expert'))


class ProjectForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Build me a website'}))
    # description=forms.(widget=forms.TextInput(attrs={'placeholder': 'Long description'}))
    price_min=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Minimum price'}))
    price_max=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Maximum price'}))
    # skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Skills'}))
    upload_files=forms.FileField(widget=forms.FileInput())
    admit_time=forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'))
    # admit_time=forms.DateField(widget = forms.SelectDateWidget())
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['price_min'].widget.attrs['min'] = 10   
 
    class Meta:
        model=Project
        fields=['title','description','price_min','price_max','level','skills','upload_files','currency','price_type','admit_time']
        widgets = {
            'description':forms.Textarea(attrs={
                
                'placeholder': 'Describe your project here...'
            }),
            'level':forms.RadioSelect(),
            'currency':forms.Select(attrs={
                'placeholder':'select'
            })
        }
class RepliesForm(forms.ModelForm): 
    class Meta:
        model=Replies
        fields=['reply','duration','price']
        widgets = {
            'duration':forms.NumberInput(attrs={
                'placeholder': 'Enter number of days'
            }),
            'price':forms.NumberInput(attrs={
                'placeholder':'Enter bid amount'
            }),
            'reply':forms.Textarea(attrs={
                'placeholder':'What makes you the best candidate for this project?'
            }),
            

        }



class FilterForm(forms.ModelForm):
    
    search = forms.CharField(required=False)
    class Meta:
        model=Project
        fields='__all__'
class ProposalsForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=()
