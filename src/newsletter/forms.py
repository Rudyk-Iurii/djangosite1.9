from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")

        #Validation
        if provider != "gmail.com":
            raise forms.ValidationError("I accept only gmail.com box")
        return email

class SignUpForm(forms.ModelForm):
    # list_display = ("__str__", "timestamp", "updated")
    class Meta:
        model = SignUp
        fields = ["full_name", 'email']
        # exclude = ["ful_name"]
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extention = provider.split(".")

        #Validation
        if provider != "gmail.com":
            raise forms.ValidationError("I accept only gmail.com box")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name