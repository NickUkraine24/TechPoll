from django.db import models
from django.conf import settings


class UsersModel(models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=60, default=None)
    surname = models.CharField(max_length=60, default=None)
    f_role = models.ForeignKey('roleAccess.RolesModel', on_delete=models.DO_NOTHING)
    # department = models.ManyToManyField('allActions.DepartmentsModel')
    f_auth = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{name} {surname}'.format(name=self.name, surname=self.surname).title()
