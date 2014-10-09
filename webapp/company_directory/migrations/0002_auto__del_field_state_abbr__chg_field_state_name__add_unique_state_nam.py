# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'State.abbr'
        db.delete_column(u'company_directory_state', 'abbr')


        # Changing field 'State.name'
        db.alter_column(u'company_directory_state', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2))
        # Adding unique constraint on 'State', fields ['name']
        db.create_unique(u'company_directory_state', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'State', fields ['name']
        db.delete_unique(u'company_directory_state', ['name'])


        # User chose to not deal with backwards NULL issues for 'State.abbr'
        raise RuntimeError("Cannot reverse this migration. 'State.abbr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'State.abbr'
        db.add_column(u'company_directory_state', 'abbr',
                      self.gf('django.db.models.fields.CharField')(max_length=2),
                      keep_default=False)


        # Changing field 'State.name'
        db.alter_column(u'company_directory_state', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'company_directory.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'capital': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company_directory.State']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'company_directory.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        }
    }

    complete_apps = ['company_directory']