from django.db import models


class PermissionsModel(models.Model):
    class Meta:
        db_table = 'permissions'

    code_name = models.CharField(max_length=60, default='null')


class RolesModel(models.Model):
    class Meta:
        db_table = 'roles'

    name = models.CharField(max_length=60, default=None)
    permissions = models.ManyToManyField('PermissionsModel')

