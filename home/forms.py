from django import forms
from home.models import Project,Currency ,PRICE_TYPES,Replies
from django.forms import Form, ChoiceField
from inbox.models import Group
from django.contrib.admin import widgets                                       
from django.contrib.admin.widgets import AdminDateWidget
from accounts.models import Skill
from django.forms.widgets import SelectDateWidget

class ProjectForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write your project title','class':'form-control','title':"Add your project title"}),min_length=3)
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Long description'}),min_length=20)
    price_min=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Minimum price'}))
    price_max=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Maximum price'}))
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),widget = forms.CheckboxSelectMultiple,error_messages={'required':"Bacarıq əlavə edin"})

    upload_files=forms.FileField(widget=forms.FileInput())
    admit_time=forms.DateField(widget=forms.SelectDateWidget())

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['price_min'].widget.attrs['min'] = 10   
   

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        existing = Project.objects.filter(title__iexact=self.cleaned_data['title'])
        price_min=cleaned_data['price_min']
        price_max=cleaned_data['price_max']
        difference=price_max-price_min
        if difference < 0:
              raise forms.ValidationError('Minimum price should not be greater than maximum price')
        if difference == 0:
              raise forms.ValidationError('Minimum price should not be equal to maximum price')
        if existing.exists():
            raise forms.ValidationError('A project with that title already exists.')

        if cleaned_data['skills'].count() < 3:
            raise forms.ValidationError('You should add minimum 3 skills.')

        
        return self.cleaned_data






    class Meta:
        model=Project
        fields=['title','description','price_min','price_max','level','skills','upload_files','currency','price_type','admit_time']
        widgets = {            
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
