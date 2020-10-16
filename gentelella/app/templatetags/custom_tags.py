'''
Created on Dec 14, 2018

@author: b.dimitriadis
'''

from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def lang_to_flag(context, lang=None, *args, **kwargs):
    lang_flag_dict = {"el": "gr", "en": "gb"}
    return lang_flag_dict.get(lang)


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
