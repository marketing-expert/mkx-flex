# visitors.views.py

from django.views import generic
from django.contrib.messages import views
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt

from visitors import mixins


@method_decorator(xframe_options_exempt, name='dispatch')
class VisitorCreateView(
    views.SuccessMessageMixin,
    mixins.VisitorEditMixin, generic.CreateView
):
    success_message = "Visitor successfully added !"
    template_name = "index.html"


visitor_create_view = VisitorCreateView.as_view(
    extra_context={"page_title": "add visitor"}
)
