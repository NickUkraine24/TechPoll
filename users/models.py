from django.db import models


class UsersModel(models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=60, default=None)
    surname = models.CharField(max_length=60, default=None)
    f_role = models.ForeignKey('roleAccess.RolesModel', on_delete=models.DO_NOTHING)
    department = models.ManyToManyField('allActions.DepartmentsModel')
