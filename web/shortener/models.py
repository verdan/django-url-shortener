import re

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.text import slugify


class SecretWord(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    last_used = models.DateTimeField(auto_now=True)
    is_consumed = models.BooleanField(default=False)

    def mark_as_consumed(self):
        self.is_consumed = True
        self.save()

    @staticmethod
    def unconsumed_secret_word(related_to_url):
        result = None
        try:
            words_in_long_url = list(map(slugify, re.findall(r"[\w']+", related_to_url)))
            result = SecretWord.objects.filter(slug__in=words_in_long_url, is_consumed=False)[0]
            if not result:
                result = SecretWord.objects.filter(is_consumed=False)[0]
        except:
            pass
        return result

    @staticmethod
    def oldest_consumed_secret_word():
        try:
            return SecretWord.objects.filter(is_consumed=True).order_by('last_used')[0]
        except:
            pass

    @staticmethod
    def get_slugs_list_of_all_secret_words():
        return SecretWord.objects.all().values_list('slug', flat=True)


class TinyUrl(models.Model):
    belongs_to = models.URLField()
    linked_with = models.OneToOneField('SecretWord', related_name='tinny_url', null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.IPAddressField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def mark_as_inactive(self):
        self.is_active = False
        self.linked_with = None
        self.save()

    @staticmethod
    def get_active_tiny_url_with_belongs_to(belongs_to):
        try:
            return TinyUrl.objects.get(belongs_to=belongs_to, is_active=True)
        except ObjectDoesNotExist:
            pass

    @staticmethod
    def get_active_tiny_url_with_slug(linked_with_slug):
        try:
            return TinyUrl.objects.get(linked_with__slug=linked_with_slug, is_active=True)
        except ObjectDoesNotExist:
            pass

    @staticmethod
    def create_tiny_url(belongs_to, linked_with):
        new_tiny_url =  TinyUrl(belongs_to=belongs_to, linked_with=linked_with)
        new_tiny_url.save()
        return new_tiny_url

