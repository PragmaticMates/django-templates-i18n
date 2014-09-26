django-templates-i18n
=====================

App provides ability to store templates in database and localize it using django-modeltranslation app.
It is useful if you need to change template content too often and you don't want to recompile all ugettext messages
all the times. It is also suitable for email templates.

Tested on Django 1.4.5.


Requirements
------------
- Django
- django-modeltranslation


Installation
------------

1. Install python library using pip: ``pip install django-templates-i18n``

2. Add ``templates_i18n`` to ``INSTALLED_APPS`` in your Django settings file

3. Sync and migrate your database

4. Specify desired languages in your Django settings file::

    from django.utils.translation import gettext

    LANGUAGE_CODE = 'en'
    LANGUAGES = (
        ('en', gettext('English')),
        ('de', gettext('German')),
    )

5. Run ``sync_translation_fields`` and ``update_translation_fields`` commands (from ``modeltranslation`` app)


Usage
-----

You can pass it to template renderer as follows::

    from django.http import HttpResponse
    from django.template import Template, Context
    from django.views.generic import View

    from templates_i18n.models import Template_i18n


    class MyView(View):
        def dispatch(self, request, *args, **kwargs):
            template_i18n = Template_i18n.objects.get(machine_name='my-template')
            template = Template(template_i18n.content)
            context = Context({'user': request.user})
            return HttpResponse(template.render(context))

or you can use it to send emails as well::

    from django.core.mail import send_mail
    from django.template import Template, Context
    from templates_i18n.models import Template_i18n


    def dispatch(self, request, *args, **kwargs):
        template_i18n = Template_i18n.objects.get(machine_name='my-template')
        template = Template(template_i18n.content)
        context = Context({'user': request.user})
        message = template.render(context)
        send_mail('Subject here', message, 'from@example.com', ['to@example.com'], fail_silently=False)


Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates