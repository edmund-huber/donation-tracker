# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Choice', fields ['speedrun', 'name']
        db.delete_unique(u'tracker_choice', ['speedrun_id', 'name'])

        # Removing unique constraint on 'ChoiceOption', fields ['choice', 'name']
        db.delete_unique(u'tracker_choiceoption', ['choice_id', 'name'])

        # Removing unique constraint on 'Challenge', fields ['speedrun', 'name']
        db.delete_unique(u'tracker_challenge', ['speedrun_id', 'name'])

        # Deleting model 'ChoiceBid'
        db.delete_table(u'tracker_choicebid')

        # Deleting model 'Challenge'
        db.delete_table(u'tracker_challenge')

        # Deleting model 'ChoiceOption'
        db.delete_table(u'tracker_choiceoption')

        # Deleting model 'Choice'
        db.delete_table(u'tracker_choice')

        # Deleting model 'ChallengeBid'
        db.delete_table(u'tracker_challengebid')


    def backwards(self, orm):
        # Adding model 'ChoiceBid'
        db.create_table(u'tracker_choicebid', (
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('donation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation_tracker.Donation'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bids', to=orm['donation_tracker.ChoiceOption'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'donation_tracker', ['ChoiceBid'])

        # Adding model 'Challenge'
        db.create_table(u'tracker_challenge', (
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
            ('goal', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('state', self.gf('django.db.models.fields.CharField')(default='OPENED', max_length=255)),
            ('speedrun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation_tracker.SpeedRun'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'donation_tracker', ['Challenge'])

        # Adding unique constraint on 'Challenge', fields ['speedrun', 'name']
        db.create_unique(u'tracker_challenge', ['speedrun_id', 'name'])

        # Adding model 'ChoiceOption'
        db.create_table(u'tracker_choiceoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(related_name='option', to=orm['donation_tracker.Choice'])),
        ))
        db.send_create_signal(u'donation_tracker', ['ChoiceOption'])

        # Adding unique constraint on 'ChoiceOption', fields ['choice', 'name']
        db.create_unique(u'tracker_choiceoption', ['choice_id', 'name'])

        # Adding model 'Choice'
        db.create_table(u'tracker_choice', (
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='OPENED', max_length=255)),
            ('speedrun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation_tracker.SpeedRun'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'donation_tracker', ['Choice'])

        # Adding unique constraint on 'Choice', fields ['speedrun', 'name']
        db.create_unique(u'tracker_choice', ['speedrun_id', 'name'])

        # Adding model 'ChallengeBid'
        db.create_table(u'tracker_challengebid', (
            ('donation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation_tracker.Donation'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('challenge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bids', to=orm['donation_tracker.Challenge'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'donation_tracker', ['ChallengeBid'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'donation_tracker.bid': {
            'Meta': {'ordering': "['event__name', 'speedrun__starttime', 'parent__speedrun__starttime', 'parent__parent__speedrun__starttime', 'parent__parent__name', 'parent__name', 'name']", 'unique_together': "(('event', 'speedrun', 'parent', 'name'),)", 'object_name': 'Bid'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bids'", 'null': 'True', 'to': u"orm['donation_tracker.Event']"}),
            'goal': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'istarget': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'options'", 'null': 'True', 'to': u"orm['donation_tracker.Bid']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'speedrun': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bids'", 'null': 'True', 'to': u"orm['donation_tracker.SpeedRun']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'OPENED'", 'max_length': '32'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'donation_tracker.donation': {
            'Meta': {'ordering': "['-timereceived']", 'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'bidstate': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '255'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'commentstate': ('django.db.models.fields.CharField', [], {'default': "'ABSENT'", 'max_length': '255'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'domain': ('django.db.models.fields.CharField', [], {'default': "'LOCAL'", 'max_length': '255'}),
            'domainId': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '160', 'blank': 'True'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.Donor']", 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.Event']"}),
            'fee': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '20', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modcomment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'readstate': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '255'}),
            'testdonation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timereceived': ('django.db.models.fields.DateTimeField', [], {}),
            'transactionstate': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '64'})
        },
        u'donation_tracker.donationbid': {
            'Meta': {'ordering': "['-donation__timereceived']", 'object_name': 'DonationBid'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'bid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bids'", 'to': u"orm['donation_tracker.Bid']"}),
            'donation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bids'", 'to': u"orm['donation_tracker.Donation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'donation_tracker.donor': {
            'Meta': {'ordering': "['lastname', 'firstname', 'email']", 'object_name': 'Donor'},
            'addresscity': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'addresscountry': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'addressstate': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'addressstreet': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'addresszip': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'paypalemail': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'prizecontributoremail': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'prizecontributorwebsite': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'runnertwitch': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'runnertwitter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'runneryoutube': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.CharField', [], {'default': "'FULL'", 'max_length': '32'})
        },
        u'donation_tracker.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paypalcurrency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '8'}),
            'paypalemail': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'receivername': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'schedulecommentatorsfield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'schedulecommentsfield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'scheduledatetimefield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'scheduleestimatefield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'schedulegamefield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'scheduleid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'schedulerunnersfield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'schedulesetupfield': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'scheduletimezone': ('django.db.models.fields.CharField', [], {'default': "'US/Eastern'", 'max_length': '64', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'targetamount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'usepaypalsandbox': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'donation_tracker.prize': {
            'Meta': {'ordering': "['event__date', 'sortkey', 'name']", 'unique_together': "(('category', 'winner', 'event'),)", 'object_name': 'Prize'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.PrizeCategory']", 'null': 'True', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'prizescontributed'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['donation_tracker.Donor']"}),
            'deprecated_provided': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'emailsent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endrun': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'prize_end'", 'null': 'True', 'to': u"orm['donation_tracker.SpeedRun']"}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'maximumbid': ('django.db.models.fields.DecimalField', [], {'default': "'5.0'", 'max_digits': '20', 'decimal_places': '2'}),
            'minimumbid': ('django.db.models.fields.DecimalField', [], {'default': "'5.0'", 'max_digits': '20', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'randomdraw': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sortkey': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'startrun': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'prize_start'", 'null': 'True', 'to': u"orm['donation_tracker.SpeedRun']"}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sumdonations': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.Donor']", 'null': 'True', 'blank': 'True'})
        },
        u'donation_tracker.prizecategory': {
            'Meta': {'object_name': 'PrizeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'donation_tracker.speedrun': {
            'Meta': {'ordering': "['event__date', 'sortkey', 'starttime']", 'unique_together': "(('name', 'event'),)", 'object_name': 'SpeedRun'},
            'deprecated_runners': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation_tracker.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'runners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['donation_tracker.Donor']", 'null': 'True', 'blank': 'True'}),
            'sortkey': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'donation_tracker.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prepend': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['donation_tracker']