from django.db import models


class SectionsModel(models.Model):
    class Meta:
        db_table = 'sections'

    def sectionslogic(self) -> int:
        res = StagesModel.objects.filter(f_section_id=self.id).first().id
        return res

    name = models.CharField(max_length=60, default=None)


class StagesModel(models.Model):
    class Meta:
        db_table = 'stages'

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
    hint = models.TextField(max_length=300, null=True, blank=True)
    f_stage = models.ForeignKey('StagesModel', on_delete=models.DO_NOTHING)
    # department = models.ManyToManyField('DepartmentsModel')


class GradesModel(models.Model):
    class Meta:
        db_table = 'grades'

    name = models.CharField(max_length=60, default=None)
