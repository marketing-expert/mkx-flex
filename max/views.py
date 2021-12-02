# max.views.py

from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from max import models, mixins


class MaxDashboard(generic.TemplateView):
    template_name = "max/max_dashboard.html"
    extra_context= {
        "app_name": "max",
        "page_title": "dashboard"
    }


max_dashboard = MaxDashboard.as_view()


class MaxSouscriberCreate(
    LoginRequiredMixin,
    mixins.SouscriberEditMixin,
    generic.CreateView
):
    model = models.Souscriber
    paginate_by = 15
    template_name = 'max/max_souscriber_create.html'
    
    def get_queryset(self):
        return super().get_queryset()
    

max_suscriber_create = MaxSouscriberCreate.as_view(
    extra_context={
        "app_name": "max",
        "page_title": "ajouter un client"
    }
)


class MaxSoucriberUpdate(
    LoginRequiredMixin,
    mixins.SouscriberEditMixin,
    generic.UpdateView
):
    model = models.Souscriber
    template_name = 'max/max_souscriber_create.html'


max_suscriber_update = MaxSoucriberUpdate.as_view(
    extra_context={
        "app_name": "max",
        "page_title": "mettre à jour"
    }
)


class MaxSouscriberList(mixins.MaxFilterMixin, generic.ListView):
    paginate_by = 15
    model = models.Souscriber
    context_object_name = 'object_souscriber_list'
    template_name = 'max/max_souscriber_list.html'


max_soucriber_list = MaxSouscriberList.as_view(
    extra_context={
        "app_name": "max",
        "page_title": "vérifier votre inscription"
    }
)


class MaxSouscriberDetail(generic.DetailView):
    model = models.Souscriber
    template_name = 'max/max_souscriber_detail.html'


max_souscriber_detail = MaxSouscriberDetail.as_view(
    extra_context={
        "app_name": "max"
    }
)


class SearchView(mixins.MaxFilterMixin, generic.ListView):
    paginate_by = 15
    model = models.Souscriber
    context_object_name = 'object_souscriber_list'
    template_name = 'max/max_souscriber_search.html'
    success_url = reverse_lazy('max:max_list_path')


search_view = SearchView.as_view(
    extra_context={
        "app_name": "max",
        "page_title": "vérifier votre inscription"
    }
)