# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TeamResponseHistory.average_score'
        db.alter_column(u'responses_teamresponsehistory', 'average_score', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5))

        # Changing field 'TeamResponseHistory.word_list'
        db.alter_column(u'responses_teamresponsehistory', 'word_list', self.gf('django.db.models.fields.CharField')(max_length=511))

    def backwards(self, orm):

        # Changing field 'TeamResponseHistory.average_score'
        db.alter_column(u'responses_teamresponsehistory', 'average_score', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TeamResponseHistory.word_list'
        db.alter_column(u'responses_teamresponsehistory', 'word_list', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'responses.teamresponsehistory': {
            'Meta': {'object_name': 'TeamResponseHistory'},
            'archive_date': ('django.db.models.fields.DateField', [], {}),
            'average_score': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.TeamTemperature']"}),
            'responder_count': ('django.db.models.fields.IntegerField', [], {}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'word_list': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        u'responses.teamtemperature': {
            'Meta': {'object_name': 'TeamTemperature'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.User']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'responses.temperatureresponse': {
            'Meta': {'object_name': 'TemperatureResponse'},
            'archive_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.TeamTemperature']"}),
            'responder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.User']"}),
            'response_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'responses.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'})
        }
    }

    complete_apps = ['responses']