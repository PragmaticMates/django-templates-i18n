from django.http import HttpResponse
from django.template import Template, Context
from django.views.generic import View, TemplateView

from templates_i18n.models import Template_i18n


class HomeView(TemplateView):
    template_name = 'home.html'


class MyView(View):
    def dispatch(self, request, *args, **kwargs):
        template_i18n = Template_i18n.objects.get(machine_name='my-template')
        template = Template(template_i18n.content)
        context = Context({'user': request.user})
        rendered_content = template.render(context)
        return HttpResponse(rendered_content)
