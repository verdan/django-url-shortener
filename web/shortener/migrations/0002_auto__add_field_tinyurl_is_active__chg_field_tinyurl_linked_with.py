# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TinyUrl.is_active'
        db.add_column(u'shortener_tinyurl', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'TinyUrl.linked_with'
        db.alter_column(u'shortener_tinyurl', 'linked_with_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['shortener.SecretWord']))

    def backwards(self, orm):
        # Deleting field 'TinyUrl.is_active'
        db.delete_column(u'shortener_tinyurl', 'is_active')


        # Changing field 'TinyUrl.linked_with'
        db.alter_column(u'shortener_tinyurl', 'linked_with_id', self.gf('django.db.models.fields.related.OneToOneField')(default=1, unique=True, to=orm['shortener.SecretWord']))

    models = {
        u'shortener.secretword': {
            'Meta': {'object_name': 'SecretWord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_consumed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_used': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'shortener.tinyurl': {
            'Meta': {'object_name': 'TinyUrl'},
            'added_by': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'belongs_to': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'linked_with': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'tinny_url'", 'unique': 'True', 'null': 'True', 'to': u"orm['shortener.SecretWord']"})
        }
    }

    complete_apps = ['shortener']