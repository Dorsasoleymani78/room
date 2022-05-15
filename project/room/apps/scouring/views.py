 
from dataclasses import fields
from re import template
from urllib import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Appraiser, Evalution,Criterion,CriterionScore
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def home(request):
    context={
        'NAME':'dORSA SOLEYMANI'
    }
    return render(request,'scouring/main.html',context)

def is_member(user):
    return user.groups.filter(name='teacher').exists()

def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['appraiser1','teacher']).exists()


class EvaluationList(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=Evalution
    template_name='scouring/evaluation.html'
    context_object_name='evalutions'
    def get_queryset(self) :
        current_user= self.request.user
        appraisers=Appraiser.objects.get(user_id= current_user.id)
        
        return  Evalution.objects.all().filter(appraiser_id=appraisers.id)
    
    def test_func(self)  :
        return  is_in_multiple_groups(self.request.user)
    
class EvaluationCreate(LoginRequiredMixin,CreateView):
    model=Evalution
    fields='__all__'
    template_name='scouring/register_evaluation.html'
    success_url='/scouring/Evaluation'
    def get_form(self,*args,**kwargs) :
        form=super(EvaluationCreate,self).get_form(*args,**kwargs)
        form.fields['appraiser'].queryset=Appraiser.objects.filter(user_id=self.request.user.id)
        appraise_typeId=Appraiser.objects.get(user_id=self.request.user.id).appraiser_type_id
        criterions=Criterion.objects.all().filter(appraiser_type_id=appraise_typeId)
        criterionIdList=[item.id for item in criterions]
        form.fields['criterion_score'].queryset=CriterionScore.objects.filter(Criterion_id__in=criterionIdList)
        return form
