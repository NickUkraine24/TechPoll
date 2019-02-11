from django.db import models


class ExpertReviewsModel(models.Model):
    class Meta:
        db_table = 'expert_reviews'

    f_answer = models.ForeignKey('AnswersModel', on_delete=models.CASCADE)
    f_grade = models.ForeignKey('allActions.GradesModel', on_delete=models.DO_NOTHING)
    comment = models.TextField(max_length=250, default=None)
    f_user_expert = models.ForeignKey('users.UsersModel', on_delete=models.DO_NOTHING)


class AnswersModel(models.Model):
    class Meta:
        db_table = 'answers'

    f_user = models.ForeignKey('users.UsersModel', on_delete=models.CASCADE, null=True, related_name='f_user')
    f_question = models.ForeignKey('allActions.QuestionsModel', on_delete=models.DO_NOTHING)
    answer_like = models.BooleanField()
    # f_expert = models.ForeignKey('users.UsersModel', on_delete=models.DO_NOTHING, null=True, related_name='f_expert')
    f_grade = models.ForeignKey('allActions.GradesModel', on_delete=models.DO_NOTHING)



