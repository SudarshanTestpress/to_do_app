from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('projects/',views.ProjectListView.as_view(), name = 'list_project'),
    path('projects/<str:pk>',views.TaskListView.as_view(), name= 'list_task'),
    path('projects/<str:pk>/updatename',views.ProjectUpdateView.as_view(), name = 'update_project'),
    path('projects/<str:pk>/deletename', views.ProjectDeleteView.as_view(), name = 'delete_project')
    
    ]