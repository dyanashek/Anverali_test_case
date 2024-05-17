from django import forms

def validate_phone_number(value: str) -> None:
    if value.count('+') > 1 or not value.replace('+', '').isdecimal() or len(value) < 6:
        raise forms.ValidationError(
            'Phone number should contain only digits and +. Should be more then 6 digits.',
            params={'value': value},
        )