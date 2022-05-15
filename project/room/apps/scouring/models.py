 
 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
from django.core import validators
 
    
#مدل مدرس
class Teacher(models.Model):
    name=models.TextField(max_length=10,verbose_name='نام')
    family=models.TextField(max_length=30,verbose_name='نام خانوادگی')
    age=models.IntegerField( verbose_name='سن',validators=[validators.MaxValueValidator(40,message="the value is too long")])
    mobile_number=models.CharField(max_length=30,verbose_name='شماره موبایل')
    is_active=models.BooleanField(default=False,null=True,verbose_name='غیرفعال/فعال')
    slug=models.SlugField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return  self.name+" "+self.family+" "+str(self.age)+" "+self.mobile_number
    
    class Meta:
        verbose_name='مدرس'
        verbose_name_plural='مدرس ها'
        ordering=['family','name']
        db_table='T_Teacher'

class Student(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    family=models.CharField(max_length=30,verbose_name='نام خانوادگی')
    mobile_number=models.CharField(max_length=30,verbose_name='شماره موبایل')
    is_active=models.BooleanField(default=False,null=True,verbose_name='غیرفعال/فعال')
    slug=models.SlugField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return  self.name+" "+self.family+" "+self.mobile_number
    
    class Meta:
        verbose_name="دانشجو"
        verbose_name_plural="دانشجویان"
        ordering=['family','name']
        db_table='T_Student'
        
class Term(models.Model):
    term_title=models.CharField(max_length=50,verbose_name='عنوان دوره')
    term_description=models.TextField(verbose_name='توضیحات دوره')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد دوره')
    start_at=models.DateTimeField(default=timezone.now,verbose_name='تاریخ شروع دوره')
    update_at=models.DateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,verbose_name='مدرس دوره')
    is_active=models.BooleanField(default=False,null=True,verbose_name='غیرفعال/فعال')
    slug=models.SlugField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return  self.term_title
    
    class Meta:
        verbose_name="دوره"
        verbose_name_plural="دوره ها"
        ordering=['term_title']  
        db_table='T_Term'
        
        
        
#مدل دوره
class TermStudent(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='دانشجو')
    term=models.ForeignKey(Term,on_delete=models.CASCADE,verbose_name='دوره')
    register_date=models.DateTimeField(verbose_name='تاریخ ثبت نام',default=timezone.now)
    
    def __str__(self) -> str:
        return  str(self.student)+"\n"+str(self.term)
 
    class Meta:
        verbose_name='دانشجوی دوره'
        verbose_name_plural='دانشجویان دوره '
        unique_together=(('student','term'),)
        db_table='T_TermStudent'

        
class AppraiserType(models.Model):
    appraiser_type_id=models.IntegerField(primary_key=True,verbose_name='کد نوع ارزیاب')
    appraiser_type_title=models.CharField(max_length=100,verbose_name='نام نوع ارزیاب')
    
    def __str__(self) -> str:
        return self.appraiser_type_title
    
    class Meta:
        verbose_name='نوع ارزیاب'
        verbose_name_plural='انواع ارزیاب'
        db_table='T_AppraiserType'
 
        
        

class Appraiser(models.Model):
    appraiser_type=models.ForeignKey(AppraiserType,on_delete=models.CASCADE,verbose_name='نوع ارزیاب')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    
    def __str__(self) -> str:
        return str(self.user)+" "+str(self.appraiser_type)
    
    class Meta:
        verbose_name='ارزیاب'
        verbose_name_plural='ارزیاب ها'
        db_table='T_Appraiser'
    
#مدل معیار
class Criterion(models.Model):
   
    Criterion_title=models.TextField(max_length=100,verbose_name='عنوان معیار')
    Criterion_description=models.TextField(max_length=300,verbose_name='توضیحات')
    appraiser_type=models.ForeignKey(AppraiserType,verbose_name='کد ارزیاب',on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return str(self.appraiser_type)+"-"+str(self.Criterion_title)
    class Meta:
        verbose_name='معیار'
        verbose_name_plural='معیار ها'
        db_table='T_Criterion'
 
        
    
#مدل امتیازات معیار
class CriterionScore(models.Model):
 
    Criterion=models.ForeignKey(Criterion,verbose_name='معیار',on_delete=models.CASCADE)
    Score_title=models.TextField(max_length=100,verbose_name='عنوان امتیاز')
    Score_value=models.IntegerField(default=0,verbose_name=' امتیاز')
    
    def __str__(self) -> str:
        return self.Score_title+" : "+str(self.Score_value)
    class Meta:
        verbose_name='امتیاز معیار '
        verbose_name_plural='امتیاز  معیار ها '
        db_table='T_CriterionScore'
    

#ارزیابی
class Evalution(models.Model):
    appraiser=models.ForeignKey(Appraiser,on_delete=models.CASCADE,verbose_name='کد ارزیاب')
    Student=models.ForeignKey(Student,verbose_name='کد دانشجو',on_delete=models.CASCADE)
    register_date=models.DateField(auto_now_add=True,verbose_name='تاریخ')
    criterion_score=models.ForeignKey(CriterionScore,verbose_name='امتیاز',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.appraiser)+"-"+str(self.Student)+"-"+str(self.criterion_score)
    
    class Meta:
        verbose_name='ارزیابی '
        verbose_name_plural='ارزیابی ها '
        db_table='T_Evalution'
   
 
    
 
 