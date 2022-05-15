 
 
from django.contrib import admin
from apps.scouring.models import *

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    List_display=('name','family','age','email','slug')
    List_filter=('family',)
    search_field=('family','name')
    ordering=['family','name']
    prepopulated_fields={'slug':('name','family')}
 
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    List_display=('name','family','mobile_number','is_active')
    List_filter=('family',)
    search_field=('family','name')
    ordering=['family','name']
    prepopulated_fields={'slug':('name','family')}
@admin.register(Term)
class LessonStudentAdmin(admin.ModelAdmin):
    List_display=('term_title','start_at','update_at','teacher','is_active' )
    List_filter=('is_active',)
    search_field=('term_title',)
    ordering=['term_title']
    prepopulated_fields={'slug':('term_title','teacher')}
    
@admin.register(TermStudent)
class TermStudentAdmin(admin.ModelAdmin):
    List_display=('student','term','register_date')
    List_filter=('student','term')
    search_field=('student','term')
    ordering=['student','term']
    
@admin.register(AppraiserType)
class AppraiserTypeAdmin(admin.ModelAdmin):
    List_display=('appraiser_type_id','appraiser_type_title')
    List_filter=('appraiser_type_title')
    search_field=('appraiser_type_title')
    ordering=['appraiser_type_title']

@admin.register(Appraiser)
class AppraiserAdmin(admin.ModelAdmin):
    List_display=('appraiser_type','user')
    List_filter=('appraiser_type')
    search_field=('appraiser_type','user')
    ordering=['appraiser_type']
    
@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    List_display=(' Criterion_title',' appraiser_type' )
    List_filter=('Criterion_title',' appraiser_type')
    search_field=('Criterion_title',)
    ordering=['Criterion_title']
 
@admin.register( CriterionScore)
class CriterionScoreAdmin(admin.ModelAdmin):
    List_display=('Criterion','Score_title','Score_value' )
    List_filter=('Criterion','Score_title')
    search_field=('Score_title',)
    ordering=['Score_title']
    

   
# @admin.register(Evalution)
# class AssessmentAdmin(admin.ModelAdmin):
#     List_display=('appraiser','Student','register_date','criterion_score' )