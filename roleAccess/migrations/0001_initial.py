from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(default='null', max_length=60)),
            ],
            options={
                'db_table': 'permissions',
            },
        ),
        migrations.CreateModel(
            name='RolesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('permissions', models.ManyToManyField(to='roleAccess.PermissionsModel')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
    ]
