from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allActions', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_like', models.BooleanField()),
                ('f_expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='f_expert', to='users.UsersModel')),
                ('f_grade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.GradesModel')),
                ('f_question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.QuestionsModel')),
                ('f_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='f_user', to='users.UsersModel')),
            ],
            options={
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='ExpertReviewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=None, max_length=250)),
                ('f_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answers.AnswersModel')),
                ('f_grade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.GradesModel')),
                ('f_user_expert', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.UsersModel')),
            ],
            options={
                'db_table': 'expert_reviews',
            },
        ),
    ]
