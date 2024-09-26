import random
from .views import ProjectListView, TaskListView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView, TaskCreateView
from django.test import TestCase
from django.http import response
from django.urls import reverse, resolve
from .models import Task, Project
from .forms import ProjectForm


# Create your tests here.

class ModelTest(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name = 'Deployment'

        )

        self.task1 = Task.objects.create(
            text = 'Eat',
            project = self.project1,
            completed = True
        )

        self.task2 = Task.objects.create(
            text = 'Sleep',
            project = self.project1,
            completed = False
        )

        self.project2 = Project.objects.create(
            name = 'Testing'

        )

        self.task3 = Task.objects.create(
            text = 'Play',
            project = self.project2,
            completed = False
        )

        self.task4 = Task.objects.create(
            text = 'Sleep',
            project = self.project2,
            completed = False
        )

    def test_model_task(self):
        self.task5 = Task.objects.create(
            text = 'Analyze data',
            project = self.project1,
            completed = False
        )

        number_of_tasks_after_test_create = Task.objects.all().count()

        self.assertEquals(number_of_tasks_after_test_create, 5)

    def test_model_project(self):
        self.project3 = Project.objects.create(
            name = 'New features'
        )

        number_of_projects_after_test_create = Project.objects.all().count()

        self.assertEquals(number_of_projects_after_test_create,3)



class TestProjectListView(TestCase):   
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment')

        

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )

            self.url = reverse('tasks:list_project')
            self.response = self.client.get(self.url)


    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)


    def test_project_list_object_is_served(self):
        view = resolve('/projects/')
        self.assertEquals(view.func.view_class, ProjectListView)


class TestTaskListView(TestCase):
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment')

        

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )


            self.url = reverse('tasks:list_task',args=[self.project1.pk])
            self.response = self.client.get(self.url)
    
    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_task_list_object_is_served(self):
        view = resolve('/projects/1/tasks')
        self.assertEquals(view.func.view_class, TaskListView)


class TestProjectCreateView(TestCase):
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment'
            )

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )


            self.url = reverse('tasks:create_project')
            self.response = self.client.get(self.url)
    
    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_project_create_object_is_served(self):
        view = resolve('/projects/create')
        self.assertEquals(view.func.view_class, ProjectCreateView)

    def test_presence_of_csrf(self):
        url = reverse('tasks:create_project')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')


class TestProjectUpdateView(TestCase):
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment'
            )

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )


            self.url = reverse('tasks:update_project',kwargs={'pk':self.project1.pk})
            self.response = self.client.get(self.url)
    
    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_project_update_object_is_served(self):
        view = resolve('/projects/1/updatename')
        self.assertEquals(view.func.view_class, ProjectUpdateView)

    def test_presence_of_csrf(self):
        url = reverse('tasks:update_project', args=[self.project1.pk])
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')


class TestProjectDeleteView(TestCase):
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment'
            )

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )


            self.url = reverse('tasks:delete_project',kwargs={'pk':self.project1.pk})
            self.response = self.client.get(self.url)
    
    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_project_delete_object_is_served(self):
        view = resolve('/projects/1/delete')
        self.assertEquals(view.func.view_class, ProjectDeleteView)

    def test_presence_of_csrf(self):
        url = reverse('tasks:delete_project', args=[self.project1.pk])
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

class TestTaskCreateView(TestCase):
    def setUp(self):
            self.project1 = Project.objects.create(
            name = 'Deployment'
            )

            self.task1 = Task.objects.create(
                text = 'Eat',
                project = self.project1,
                completed = True
            )

            self.task2 = Task.objects.create(
                text = 'Sleep',
                project = self.project1,
                completed = False
            )


            self.url = reverse('tasks:create_task', args=[self.project1.pk])
            self.response = self.client.get(self.url)
    
    def test_page_serve_successful(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_task_create_object_is_served(self):
        view = resolve('/projects/1/tasks/create')
        self.assertEquals(view.func.view_class, TaskCreateView)

    def test_presence_of_csrf(self):
        url = reverse('tasks:create_task', args=[self.project1.pk])
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')