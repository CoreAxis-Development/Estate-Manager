from django.forms import ModelForm , ModelMultipleChoiceField , CheckboxSelectMultiple , TextInput , EmailInput
from .models import Contact , ContactType

class ContactSaveForm(ModelForm):

    class Meta:
        model = Contact

        fields = ['first_name' , 'last_name' , 'contact' , 'company_name' , 'email', 'type' ]

        widgets = {
            'first_name' : TextInput(attrs = {"class" : "underline-text-field"}),
            'last_name' : TextInput(attrs = {"class" : "underline-text-field"}),
            'contact' : TextInput(attrs = {"class" : "underline-text-field"}),
            'company_name' : TextInput(attrs = {"class" : "underline-text-field"}),
            'email' : EmailInput(attrs = {"class" : "underline-text-field"}),
          
        }
    
    type = ModelMultipleChoiceField(
        queryset= ContactType.objects.all(),
        widget= CheckboxSelectMultiple,
        
    )
