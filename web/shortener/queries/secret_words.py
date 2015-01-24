import re

from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from web.shortener.models import SecretWord


base_model = SecretWord


def unconsumed_secret_word(related_to_url):
    result = None
    try:
        words_in_long_url = list(map(slugify, re.findall(r"[\w']+", related_to_url)))
        result = base_model.objects.get(slug__in=words_in_long_url, is_consumed=False)
        if not result:
            result = base_model.objects.get(is_consumed=False)
    except ObjectDoesNotExist:
        pass
    return result


def oldest_consumed_secret_word():
    try:
        return base_model.objects.get(is_consumed=True).order_by('last_used')
    except ObjectDoesNotExist:
        pass
