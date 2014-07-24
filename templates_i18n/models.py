from django.db import models
from django.utils.translation import ugettext_lazy as _


class Template_i18n(models.Model):
    machine_name = models.CharField(_(u'machine name'), max_length=255, unique=True)
    content = models.TextField(_(u'content'), blank=True)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    class Meta:
        verbose_name = _(u'template')
        verbose_name_plural = _(u'templates')
        ordering = ('machine_name',)

    def __unicode__(self):
        return self.machine_name
