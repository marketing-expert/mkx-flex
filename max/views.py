# max.views.py

from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from max import models

@method_decorator(xframe_options_exempt, name='dispatch')
class SouscriberCreate(generic.CreateView):
    model = models.Souscriber
    paginate_by = 15
    template_name = 'max/souscriber_create.html'
    
    def get_queryset(self):
        return super().get_queryset()
    

suscriber_create = SouscriberCreate.as_view()


class SouscriberList(generic.ListView):
    model = models.Souscriber
    template_name = 'max/soucriber_list.html'


soucriber_list = SouscriberList.as_view()


class SouscriberDetail(generic.DetailView):
    model = models.Souscriber
    template_name = 'max/souscriber_detail.html'


souscriber_detail = SouscriberDetail.as_view()
