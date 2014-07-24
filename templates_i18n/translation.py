from modeltranslation.translator import translator, TranslationOptions
from templates_i18n.models import Template_i18n


class TemplateTranslationOptions(TranslationOptions):
    fields = ('content', )

translator.register(Template_i18n, TemplateTranslationOptions)
