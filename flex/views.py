# visitors.views.py

from django.views import generic
from django.contrib.messages import views
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.clickjacking import xframe_options_exempt

from flex import models, mixins


class FLexDashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "flex/flex_dashboard.html"
    extra_context= {
        "app_name": "flex",
        "page_title": "dashboard"
    }


flex_dashboard = FLexDashboard.as_view()


@method_decorator(xframe_options_exempt, name='dispatch')
class FlexVisitorCreateView(
    LoginRequiredMixin,
    views.SuccessMessageMixin,
    mixins.VisitorEditMixin, generic.CreateView
):
    success_message = "Visitor successfully added !"
    template_name = "flex/flex_add_visitor.html"


flex_create_visitor_view = FlexVisitorCreateView.as_view(
    extra_context={
        "app_name": "flex",
        "page_title": "enregistrer le visiteur"
    }
)


class FlexVisitorListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 3
    model = models.Visitor
    context_object_name = "object_visitor_list"
    template_name = "flex/flex_list_visitor.html"


flex_list_visitor_view = FlexVisitorListView.as_view(
    extra_context={
        "app_name": "flex",
        "page_title": "liste des visiteurs"
    }
)
