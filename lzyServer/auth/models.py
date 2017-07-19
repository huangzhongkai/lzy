from __future__ import unicode_literals

from django.db import models

class AuthenticatingCode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    auth_code = models.CharField(db_column='AUTH_CODE', max_length=30)
    date = models.CharField(db_column='DATE',default=0, max_length=30)
    class Meta:
        db_table = 'auth_code'