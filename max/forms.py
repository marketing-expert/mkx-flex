# max.forms.py

from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from flex.models import Visitor
from max.models import Souscriber


class AddSouscriberForm(forms.ModelForm):
    gender = forms.TypedChoiceField(
        label="Civilité", choices=Visitor.GENDER_CHOICES,
        initial='1', coerce=str, required=True,
    )

    class Meta:
        model = Souscriber
        fields = "__all__"
        excludes = "created_at"

    def __init__(self, *args, **kwargs):
        super(AddSouscriberForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control shadow-none'})

            if self.fields["is_pack_easy"] and self.fields["is_pack_phoenix"] and self.fields["is_pack_silver"] and self.fields['is_pack_gold'] and self.fields['is_pack_fun']:
                self.fields['is_pack_silver'].widget.attrs.update(
                    {
                        'class': 'form-check-input shadow-none mx-2',
                        'type': 'checkbox'
                    }
                )
                self.fields['is_pack_gold'].widget.attrs.update(
                    {
                        'class': 'form-check-input shadow-none mx-2',
                        'type': 'checkbox'
                    }
                )
                self.fields['is_pack_phoenix'].widget.attrs.update(
                    {
                        'class': 'form-check-input shadow-none mx-2',
                        'type': 'checkbox'
                    }
                )
                self.fields['is_pack_easy'].widget.attrs.update(
                    {
                        'class': 'form-check-input shadow-none mx-2',
                        'type': 'checkbox'
                    }
                )
                self.fields['is_pack_fun'].widget.attrs.update(
                    {
                        'class': 'form-check-input shadow-none mx-2',
                        'type': 'checkbox'
                    }
                )
