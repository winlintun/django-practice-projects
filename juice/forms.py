from django import forms
from .models import Order


class CartForm(forms.ModelForm):
    full_name = forms.CharField(label="Full Name", max_length=100)
    address = forms.CharField(label="Address", widget=forms.Textarea)

    class Meta:
        model = Order
        exclude = ("total_price", "juices")

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
