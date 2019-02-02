from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allActions', '0001_initial'),
        ('roleAccess', '0001_initial'),
        ('allActions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('surname', models.CharField(default=None, max_length=60)),
                ('department', models.ManyToManyField(to='allActions.DepartmentsModel')),
                ('f_role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roleAccess.RolesModel')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
