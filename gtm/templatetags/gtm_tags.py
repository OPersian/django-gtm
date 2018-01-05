from django import template
from django.conf import settings

from .. models import GTMSettings


register = template.Library()


@register.inclusion_tag('gtm/gtm.html', name='gtm')
@register.inclusion_tag('gtm/gtm_head.html', name='gtm_head')
@register.inclusion_tag('gtm/gtm_body.html', name='gtm_body')
def gtm_tag(google_tag_id=None):
    google_tag_id = (
        google_tag_id or GTMSettings.load().code or getattr(settings, 'GOOGLE_TAG_ID', None)
    )

    return {
        'google_tag_id': google_tag_id
    }
