from django.db import models


class SectionsModel(models.Model):
    class Meta:
        db_table = 'sections'

    name = models.CharField(max_length=60, default=None)


class StepsModel(models.Model):
    class Meta:
        db_table = 'steps'

    title = models.CharField(max_length=60, default=None)
    f_section = models.ForeignKey('SectionsModel', on_delete=models.DO_NOTHING)


class DepartmentsModel(models.Model):
    class Meta:
        db_table = 'departments'

    name = models.CharField(max_length=60, default=None)


class QuestionsModel(models.Model):
    class Meta:
        db_table = 'questions'

    title = models.CharField(max_length=60, default=None)
    f_step = models.ForeignKey('StepsModel', on_delete=models.DO_NOTHING)


class GradesModel(models.Model):
    class Meta:
        db_table = 'grades'

    name = models.CharField(max_length=60, default=None)
