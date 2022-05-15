from django.urls import path,include
import apps.scouring.views as vs
from .views import EvaluationList,EvaluationCreate

urlpatterns=[
    path('',vs.home),
    path('Evaluation/',EvaluationList.as_view(),name='evaluation'),
    path('Evaluation/add',EvaluationCreate.as_view(),name='add')
]