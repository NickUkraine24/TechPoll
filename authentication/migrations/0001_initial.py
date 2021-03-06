from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(default=None, max_length=60)),
                ('password', models.CharField(default=None, max_length=60)),
                ('f_users', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='f_users', to='users.UsersModel')),
                ('registered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='registered_by', to='users.UsersModel')),
            ],
            options={
                'db_table': 'authentication',
            },
        ),
    ]
