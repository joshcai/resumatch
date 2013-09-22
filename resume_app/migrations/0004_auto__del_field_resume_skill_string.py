# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Resume.skill_string'
        db.delete_column(u'resume_app_resume', 'skill_string')


    def backwards(self, orm):
        # Adding field 'Resume.skill_string'
        db.add_column(u'resume_app_resume', 'skill_string',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    models = {
        u'resume_app.additional': {
            'Meta': {'object_name': 'Additional'},
            'descriptions': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.additional_section': {
            'Meta': {'object_name': 'Additional_Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume_app.Additional']", 'symmetrical': 'False'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.Resume']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.edu': {
            'Meta': {'object_name': 'Edu'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descriptions': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'finish': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'gpa': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume_app.Tag']", 'symmetrical': 'False'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.exp': {
            'Meta': {'object_name': 'Exp'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descriptions': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'finish': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume_app.Tag']", 'symmetrical': 'False'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.honor': {
            'Meta': {'object_name': 'Honor'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descriptions': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume_app.Tag']", 'symmetrical': 'False'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.info': {
            'Meta': {'object_name': 'Info'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.job': {
            'Meta': {'object_name': 'Job'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'resume_app.resume': {
            'Meta': {'object_name': 'Resume'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resume': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'skill_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.Skill_Set']"})
        },
        u'resume_app.skill_set': {
            'Meta': {'object_name': 'Skill_Set'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume_app.Tag']", 'symmetrical': 'False'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_app.User']"})
        },
        u'resume_app.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['resume_app']