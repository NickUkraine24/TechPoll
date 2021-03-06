from django.shortcuts import render, redirect
from django.views import View
from allActions.models import GradesModel, StagesModel, SectionsModel, QuestionsModel
from .models import AnswersModel


def main_action(request):
    # Navigate to cover page
    return render(request, 'allActions/main.html')


class Answers(View):
    def get(self, request, stage_id):
        # Taking a data with a Postgres by specific filter
        questions = QuestionsModel.objects.filter(f_stage_id=stage_id)
        stages = StagesModel.objects.filter(f_section_id=StagesModel.objects.get(id=stage_id).f_section)
        stage_s = StagesModel.objects.get(pk=stage_id)
        sections = SectionsModel.objects.all()
        grades = GradesModel.objects.all()
        return render(request, 'allActions/poll.html', context={
            'questions': questions,
            'stage_id': stage_id,
            'stages': stages,
            'stage_s': stage_s,
            'sections': sections,
            'grades': grades,
        })

    def post(self, request, stage_id):
        # Entering a data with a front side in Postgres with filter
        query_list = []
        questions_id = set(filter(lambda key: key.isnumeric(), map(lambda x: x[:-5], dict(request.POST).keys())))
        for question_id in questions_id:
            answer = AnswersModel()
            if request.POST[question_id+"_like"] == 'Yes':
                answer.answer_like = True
            else:
                answer.answer_like = False
            answer.f_grade = GradesModel.objects.get(name=request.POST[question_id+"grade"])
            answer.f_user_id = request.user.id
            answer.f_question_id = int(question_id)
            query_list.append(answer)
        AnswersModel.objects.bulk_create(query_list)
        # Filter for avoidance error
        if stage_id == len(StagesModel.objects.all()):
            return redirect('/{}'.format(''))
        else:
            return redirect('/{}/{}'.format('poll', stage_id+1))


class LoginPage(View):
    def get(self, request):
        # Navigate to authentication page
        return render(request, 'authentication/auth.html')
