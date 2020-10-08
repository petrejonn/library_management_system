from django import forms

from .models import Borrow


class BorrowCreateForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['user', 'book', 'extra_details']
        widgets = {'book': forms.HiddenInput()}
