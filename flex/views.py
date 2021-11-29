# visitors.views.py

from django.views import generic
from django.contrib.messages import views
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.clickjacking import xframe_options_exempt

from flex import models, mixins


class VisitorDashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    extra_context= {"page_title": "dashboard"}


visitor_dashboard = VisitorDashboard.as_view()


@method_decorator(xframe_options_exempt, name='dispatch')
class VisitorCreateView(
    LoginRequiredMixin,
    views.SuccessMessageMixin,
    mixins.VisitorEditMixin, generic.CreateView
):
    success_message = "Visitor successfully added !"
    template_name = "flex/add_visitor.html"


visitor_create_view = VisitorCreateView.as_view(
    extra_context={"page_title": "enregistrer le visiteur"}
)


class VisitorListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 3
    model = models.Visitor
    context_object_name = "object_visitor_list"
    template_name = "flex/list_visitor.html"


visitor_list_view = VisitorListView.as_view(
    extra_context={"page_title": "liste des visiteurs"}
)
