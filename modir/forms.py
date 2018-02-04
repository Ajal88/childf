from django import forms
from karbar.choice import us_type


class SendToAll(forms.Form):
    subject = forms.CharField()
    context = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'text', 'rows': '3'}))
    receiver_type = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                                              choices=us_type)
