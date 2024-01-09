
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('update/<int:id>',views.Update,name='update'),
    
    
    
    # path('contact/',views.contact,name='contact')

]
