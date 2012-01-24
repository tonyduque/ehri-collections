# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('repositories_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['repositories.Repository'])),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street_address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contact_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contact_type_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contact_type_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contact_type_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('region_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('region_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('region_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('repositories', ['Contact'])

        # Adding field 'Repository.created_at'
        db.add_column('repositories_repository', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 1, 24)), keep_default=False)

        # Adding field 'Repository.updated_at'
        db.add_column('repositories_repository', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('repositories_contact')

        # Deleting field 'Repository.created_at'
        db.delete_column('repositories_repository', 'created_at')

        # Deleting field 'Repository.updated_at'
        db.delete_column('repositories_repository', 'updated_at')


    models = {
        'repositories.contact': {
            'Meta': {'object_name': 'Contact'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'region_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'region_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'region_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['repositories.Repository']"}),
            'street_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'repositories.othername': {
            'Meta': {'object_name': 'OtherName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'other_names'", 'to': "orm['repositories.Repository']"})
        },
        'repositories.repository': {
            'Meta': {'object_name': 'Repository'},
            'authorized_form_of_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'dates_of_existence': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'functions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'functions_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'functions_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'functions_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'general_context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'general_context_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'general_context_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'general_context_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'history_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'history_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'history_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'internal_structures': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'internal_structures_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'internal_structures_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'internal_structures_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legal_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legal_status_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legal_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legal_status_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lod': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'maintenance_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance_notes_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance_notes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance_notes_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mandates': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mandates_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mandates_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mandates_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'places': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'places_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'places_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'places_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rules_conventions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rules_conventions_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rules_conventions_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rules_conventions_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_of_entity': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['repositories']
