from django.db import models


class AuthModel(models.Model):
    class Meta:
        db_table = 'authentication'

    login = models.CharField(max_length=60, default=None)
    password = models.CharField(max_length=60, default=None)
    f_users = models.OneToOneField('users.UsersModel', on_delete=models.CASCADE, related_name='f_users', null=True)
    registered_by = models.ForeignKey('users.UsersModel', on_delete=models.DO_NOTHING, related_name='registered_by', null=True)
