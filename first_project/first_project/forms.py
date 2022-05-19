from django import forms
class DegreeForm(forms.Form) :
    title = forms.CharField(label='Title', max_length=20)
    branch = forms.CharField(label='Branch', max_length=50)
    file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)')


    