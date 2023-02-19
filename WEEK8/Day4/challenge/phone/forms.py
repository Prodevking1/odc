from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)
    phone_number = PhoneNumberField(label='Phone Number', required=False)
