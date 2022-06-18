from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('project/<str:pk>/', views.project, name='project'),
    path('add-project/',views.addProject, name='add-project'),
    path('edit-project/<str:pk>/', views.editProject, name='edit-project'),
    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<str:pk>/', views.messagePage, name="message"),
    path('addSkill/', views.addSkill, name='add-skill'),
    path('addEndorsements/', views.addEndorsements, name='add-endorsement'),
    path('chart/', views.chartPage, name='chartPage'),
]