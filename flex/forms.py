# flex.forms.py

from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from flex.models import Visitor


class AddVisitorForm(forms.ModelForm):
    gender = forms.TypedChoiceField(
        label="Civilité", choices=Visitor.GENDER_CHOICES,
        initial='1', coerce=str, required=True,
    )

    class Meta:
        model = Visitor
        fields = "__all__"
        excludes = "created_at"

        widgets = {
            'hour_start_visit': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'hour_end_visit': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(AddVisitorForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control shadow-none'})
