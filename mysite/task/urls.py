from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from core.models import Task
from task import views as task_views

urlpatterns = [ url(r'^$', ListView.as_view(
                  queryset=Task.objects.all().order_by("-datetime")[:25],
                  template_name="task/all_tasks.html"), name="task"),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Task,
                  template_name="task/task.html")),
                url(r'^new/$', task_views.new_task, name='new')]
