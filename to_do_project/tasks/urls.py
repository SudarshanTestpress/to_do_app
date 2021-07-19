from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = 'tasks'

urlpatterns = [
    path('projects/',views.ProjectListView.as_view(), name = 'list_project'),
    path('projects/<str:pk>',views.TaskListView.as_view(), name= 'list_task')
    
    ]