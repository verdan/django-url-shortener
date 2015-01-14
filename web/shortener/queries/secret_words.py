import re

from django.utils.text import slugify


def unconsumed_secret_word(queryset, related_to_url):
    words_in_long_url = list(map(slugify, re.findall(r"[\w']+", related_to_url)))
    results = queryset.filter(slug__in=words_in_long_url, is_consumed=False)
    if not results:
        results = queryset.filter(is_consumed=False)
    return results


def oldest_consumed_secret_word(queryset):
    return queryset.filter(is_consumed=True).order_by('last_used')