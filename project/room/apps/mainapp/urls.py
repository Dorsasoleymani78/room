 


import apps.mainapp.views as view
from django.urls import path


urlpatterns=[
    path('',view.home,name='home')
    
]