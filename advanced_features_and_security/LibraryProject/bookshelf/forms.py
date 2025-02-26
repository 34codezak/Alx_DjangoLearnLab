from django import forms

class ExampleForm(forms.Form):
    # Add your form fields here
    field1 = forms.CharField(max_length=100)
    field2 = forms.EmailField()