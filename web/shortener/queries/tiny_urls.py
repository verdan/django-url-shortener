from django.core.exceptions import ObjectDoesNotExist

from web.shortener.models import TinyUrl


base_model = TinyUrl


def get_active_tiny_url_with_belongs_to(belongs_to):
    try:
        return base_model.objects.get(belongs_to=belongs_to, is_active=True)
    except ObjectDoesNotExist:
        pass

def get_active_tiny_url_with_slug(linked_with_slug):
    try:
        return base_model.objects.get(linked_with__slug=linked_with_slug, is_active=True)
    except ObjectDoesNotExist:
        pass

def create_tiny_url(belongs_to, linked_with):
    return base_model(belongs_to=belongs_to, linked_with=linked_with).save()