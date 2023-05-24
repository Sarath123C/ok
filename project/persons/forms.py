from django import forms

from persons.models import Person


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {'gender': forms.RadioSelect()}
