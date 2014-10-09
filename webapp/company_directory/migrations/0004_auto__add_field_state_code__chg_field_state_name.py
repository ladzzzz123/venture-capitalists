# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'State.code'
        db.add_column(u'company_directory_state', 'code',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=2),
                      keep_default=False)


        # Changing field 'State.name'
        db.alter_column(u'company_directory_state', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))

    def backwards(self, orm):
        # Deleting field 'State.code'
        db.delete_column(u'company_directory_state', 'code')


        # Changing field 'State.name'
        db.alter_column(u'company_directory_state', 'name', self.gf('django.db.models.fields.CharField')(max_length=2, unique=True))

    models = {
        u'company_directory.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'capital': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company_directory.State']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'company_directory.state': {
            'Meta': {'object_name': 'State'},
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['company_directory']