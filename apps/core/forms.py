from allauth.account.models import EmailAddress
from django import forms

from .models import User


class CustomEmailAddressAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="User")

    class Meta:
        model = EmailAddress
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            "user"
        ].label_from_instance = (
            lambda obj: f"{obj.first_name} {obj.last_name} ({obj.email})"
        )
