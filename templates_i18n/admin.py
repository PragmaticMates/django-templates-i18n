from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from models import Template_i18n


class TemplateAdmin(TranslationAdmin):
    fields = ('machine_name', 'content'),
    list_display = ('machine_name',)
    search_fields = ('machine_name', 'content')
    readonly_fields = ('created', 'modified')

admin.site.register(Template_i18n, TemplateAdmin)
