from django import forms
from django.forms import ModelForm, TextInput
from web.models import Contact
from django.forms.widgets import EmailInput
from web.models import COMPANY_SIZE, INDUSTRY_SIZE, JOB, COUNTRY

EMPTY_COMPANY_SIZE = (("", "Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("", "Industry"),) + INDUSTRY_SIZE
EMPTY_JOB = (("", "Job Role"),) + JOB
EMPTY_COUNTRY = (("", "Country"),) + COUNTRY


class ContactForm(ModelForm):
    company_size = forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job = forms.ChoiceField(choices=EMPTY_JOB)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'email': EmailInput(attrs={"placeholder": "Work Email here"}),
            'first_name': TextInput(attrs={"placeholder": "First Name "}),
            'last_name': TextInput(attrs={"placeholder": "Last Name "}),
            'company': TextInput(attrs={"placeholder": "Company Name "}),



        }
