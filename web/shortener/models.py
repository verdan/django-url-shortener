from django.db import models


class SecretWord(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    last_used = models.DateTimeField(auto_now=True)
    is_consumed = models.BooleanField(default=False)

    def mark_as_consumed(self):
        self.is_consumed = True
        self.save()


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

