# Generated by Django 2.1.5 on 2019-01-31 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190131_1913'),
        ('answers', '0002_auto_20190131_1848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepartmentsModel',
        ),
        migrations.RemoveField(
            model_name='questionsmodel',
            name='f_step',
        ),
        migrations.RemoveField(
            model_name='stepsmodel',
            name='f_section',
        ),
        migrations.AlterField(
            model_name='answersmodel',
            name='f_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.GradesModel'),
        ),
        migrations.AlterField(
            model_name='answersmodel',
            name='f_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.QuestionsModel'),
        ),
        migrations.AlterField(
            model_name='expertreviewsmodel',
            name='f_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='allActions.GradesModel'),
        ),
        migrations.DeleteModel(
            name='GradesModel',
        ),
        migrations.DeleteModel(
            name='QuestionsModel',
        ),
        migrations.DeleteModel(
            name='SectionsModel',
        ),
        migrations.DeleteModel(
            name='StepsModel',
        ),
    ]