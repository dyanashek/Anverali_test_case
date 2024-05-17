from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from .models import CustomerProfile, FreelancerProfile
from django import forms
from core.validators.validators import validate_phone_number
from core.choices.choices import GENDER, CURRENCY, SPECIALIZATION


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'sex', 'phone',) 


class CustomerProfileForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY, widget=forms.widgets.RadioSelect)

    class Meta:
        model = CustomerProfile
        fields = ('currency', )


class FreelancerProfileForm(forms.ModelForm):
    specialization = forms.MultipleChoiceField(choices=SPECIALIZATION, widget=forms.widgets.CheckboxSelectMultiple)

    class Meta:
        model = FreelancerProfile
        fields = ('specialization', )


class CustomerProfileMultiForm(MultiModelForm):
    form_classes = {
        'user': CreationForm,
        'profile': CustomerProfileForm,
    }


class FreelancerProfileMultiForm(MultiModelForm):
    form_classes = {
        'user': CreationForm,
        'profile': FreelancerProfileForm,
    }

