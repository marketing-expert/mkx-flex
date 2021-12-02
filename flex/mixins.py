# flex.mixins.py

from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect

from flex import models, forms


class VisitorEditMixin(object):
    model = models.Visitor
    initial = {'hour_start_visit': timezone.now()}
    form_class = forms.AddVisitorForm

    def get_success_url(self):
        return reverse("flex:add_visitor")

    def form_valid(self, form, *args, **kwargs):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
