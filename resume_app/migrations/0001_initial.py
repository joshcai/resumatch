# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'resume_app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'resume_app', ['User'])

        # Adding model 'Tag'
        db.create_table(u'resume_app_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
        ))
        db.send_create_signal(u'resume_app', ['Tag'])

        # Adding model 'Edu'
        db.create_table(u'resume_app_edu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('gpa', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('finish', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('descriptions', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'resume_app', ['Edu'])

        # Adding M2M table for field tags on 'Edu'
        m2m_table_name = db.shorten_name(u'resume_app_edu_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('edu', models.ForeignKey(orm[u'resume_app.edu'], null=False)),
            ('tag', models.ForeignKey(orm[u'resume_app.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['edu_id', 'tag_id'])

        # Adding model 'Exp'
        db.create_table(u'resume_app_exp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('finish', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('descriptions', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'resume_app', ['Exp'])

        # Adding M2M table for field tags on 'Exp'
        m2m_table_name = db.shorten_name(u'resume_app_exp_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exp', models.ForeignKey(orm[u'resume_app.exp'], null=False)),
            ('tag', models.ForeignKey(orm[u'resume_app.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['exp_id', 'tag_id'])

        # Adding model 'Skill_Set'
        db.create_table(u'resume_app_skill_set', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'resume_app', ['Skill_Set'])

        # Adding M2M table for field tags on 'Skill_Set'
        m2m_table_name = db.shorten_name(u'resume_app_skill_set_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('skill_set', models.ForeignKey(orm[u'resume_app.skill_set'], null=False)),
            ('tag', models.ForeignKey(orm[u'resume_app.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['skill_set_id', 'tag_id'])

        # Adding model 'Skill'
        db.create_table(u'resume_app_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.Skill_Set'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'resume_app', ['Skill'])

        # Adding model 'Honor'
        db.create_table(u'resume_app_honor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('descriptions', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'resume_app', ['Honor'])

        # Adding M2M table for field tags on 'Honor'
        m2m_table_name = db.shorten_name(u'resume_app_honor_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('honor', models.ForeignKey(orm[u'resume_app.honor'], null=False)),
            ('tag', models.ForeignKey(orm[u'resume_app.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['honor_id', 'tag_id'])

        # Adding model 'Additional'
        db.create_table(u'resume_app_additional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('descriptions', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'resume_app', ['Additional'])

        # Adding model 'Additional_Section'
        db.create_table(u'resume_app_additional_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'resume_app', ['Additional_Section'])

        # Adding M2M table for field sections on 'Additional_Section'
        m2m_table_name = db.shorten_name(u'resume_app_additional_section_sections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('additional_section', models.ForeignKey(orm[u'resume_app.additional_section'], null=False)),
            ('additional', models.ForeignKey(orm[u'resume_app.additional'], null=False))
        ))
        db.create_unique(m2m_table_name, ['additional_section_id', 'additional_id'])

        # Adding model 'Info'
        db.create_table(u'resume_app_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
        ))
        db.send_create_signal(u'resume_app', ['Info'])

        # Adding model 'Resume'
        db.create_table(u'resume_app_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('resume', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')()),
            ('skill_string', self.gf('django.db.models.fields.TextField')(default='')),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'resume_app', ['Resume'])

        # Adding model 'Comment'
        db.create_table(u'resume_app_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.Resume'])),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_app.User'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume_app', ['Comment'])

        # Adding model 'Job'
        db.create_table(u'resume_app_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'resume_app', ['Job'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'resume_app_user')

        # Deleting model 'Tag'
        db.delete_table(u'resume_app_tag')

        # Deleting model 'Edu'
        db.delete_table(u'resume_app_edu')

        # Removing M2M table for field tags on 'Edu'
        db.delete_table(db.shorten_name(u'resume_app_edu_tags'))

        # Deleting model 'Exp'
        db.delete_table(u'resume_app_exp')

        # Removing M2M table for field tags on 'Exp'
        db.delete_table(db.shorten_name(u'resume_app_exp_tags'))

        # Deleting model 'Skill_Set'
        db.delete_table(u'resume_app_skill_set')

        # Removing M2M table for field tags on 'Skill_Set'
        db.delete_table(db.shorten_name(u'resume_app_skill_set_tags'))

        # Deleting model 'Skill'
        db.delete_table(u'resume_app_skill')

        # Deleting model 'Honor'
        db.delete_table(u'resume_app_honor')

        # Removing M2M table for field tags on 'Honor'
        db.delete_table(db.shorten_name(u'resume_app_honor_tags'))

        # Deleting model 'Additional'
        db.delete_table(u'resume_app_additional')

        # Deleting model 'Additional_Section'
        db.delete_table(u'resume_app_additional_section')

        # Removing M2M table for field sections on 'Additional_Section'
        db.delete_table(db.shorten_name(u'resume_app_additional_section_sections'))

        # Deleting model 'Info'
        db.delete_table(u'resume_app_info')

        # Deleting model 'Resume'
        db.delete_table(u'resume_app_resume')

        # Deleting model 'Comment'
        db.delete_table(u'resume_app_comment')

        # Deleting model 'Job'
        db.delete_table(u'resume_app_job')


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
            'skill_string': ('django.db.models.fields.TextField', [], {'default': "''"}),
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