from django.contrib import admin
from .models import SectionsModel, StagesModel, QuestionsModel, GradesModel

admin.site.register(SectionsModel)
admin.site.register(StagesModel)
admin.site.register(QuestionsModel)
admin.site.register(GradesModel)
