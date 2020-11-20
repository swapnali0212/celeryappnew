from django import forms


class itemForm(forms.Form):
    item_name = forms.CharField(label='item_name', required=True)
    item_status = forms.CharField(label='item_status', required=True)


