# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'SecretWord'
        db.create_table(u'shortener_secretword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('last_used', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_consumed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'shortener', ['SecretWord'])

        # Adding model 'TinyUrl'
        db.create_table(u'shortener_tinyurl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('belongs_to', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('linked_with',
             self.gf('django.db.models.fields.related.OneToOneField')(related_name='tinny_url', unique=True,
                                                                      to=orm['shortener.SecretWord'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('added_by', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'shortener', ['TinyUrl'])


    def backwards(self, orm):
        # Deleting model 'SecretWord'
        db.delete_table(u'shortener_secretword')

        # Deleting model 'TinyUrl'
        db.delete_table(u'shortener_tinyurl')


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
            'added_by': (
            'django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'belongs_to': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linked_with': ('django.db.models.fields.related.OneToOneField', [],
                            {'related_name': "'tinny_url'", 'unique': 'True', 'to': u"orm['shortener.SecretWord']"})
        }
    }

    complete_apps = ['shortener']