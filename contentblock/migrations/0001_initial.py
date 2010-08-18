# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContentBlockTranslation'
        db.create_table('contentblock_contentblock_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contentblock_texts', null=True, to=orm['cms.Placeholder'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['contentblock.ContentBlock'])),
        ))
        db.send_create_signal('contentblock', ['ContentBlockTranslation'])

        # Adding unique constraint on 'ContentBlockTranslation', fields ['language_code', 'master']
        db.create_unique('contentblock_contentblock_translation', ['language_code', 'master_id'])

        # Adding model 'ContentBlock'
        db.create_table('contentblock_contentblock', (
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal('contentblock', ['ContentBlock'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ContentBlockTranslation', fields ['language_code', 'master']
        db.delete_unique('contentblock_contentblock_translation', ['language_code', 'master_id'])

        # Deleting model 'ContentBlockTranslation'
        db.delete_table('contentblock_contentblock_translation')

        # Deleting model 'ContentBlock'
        db.delete_table('contentblock_contentblock')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contentblock.contentblock': {
            'Meta': {'object_name': 'ContentBlock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        'contentblock.contentblocktranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ContentBlockTranslation', 'db_table': "'contentblock_contentblock_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['contentblock.ContentBlock']"}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contentblock_texts'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        }
    }

    complete_apps = ['contentblock']
