# max.mixins.py

from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect

from max import models, forms, filters


class SouscriberEditMixin(object):
    model = models.Souscriber
    form_class = forms.AddSouscriberForm

    def get_success_url(self):
        return reverse("max:max_list_path")

    def form_valid(self, form, *args, **kwargs):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class MaxNumberKitSearchMixin(object):
    def get_queryset(self, **kwargs):
        queryset = super(MaxNumberKitSearchMixin, self).get_queryset(**kwargs)
        query = self.request.GET.get('query', None)
        if query:
            lookups = (
                Q(number_kit__exact=query)
                | Q(phone_one__exact=query)
            )
            return queryset.filter(lookups).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query', None)
        if query:
            kwargs['page_title'] = f'Recherche pour "{query}"'
        return super(MaxNumberKitSearchMixin, self).get_context_data(**kwargs)


class MaxFilterMixin(object):

    def get_context_data(self, **kwargs):
        
        kwargs['filter'] = filters.MaxFilter(
            self.request.GET, queryset=self.get_queryset()
        )

        return super(MaxFilterMixin, self).get_context_data(**kwargs)
