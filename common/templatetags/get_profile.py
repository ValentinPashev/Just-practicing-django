from django import template
from ExamPrep_2.utils import get_profile_object

register = template.Library()

@register.simple_tag
def get_profile():
    return get_profile_object()