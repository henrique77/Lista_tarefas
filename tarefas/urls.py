from django.urls import path, include

from django.conf.urls import url
from tarefas import views

#Urls para acessar todas as tarefas ou individualmente
urlpatterns = [
    url(r'^api/tarefas$', views.tarefa_list, name='tarefas'),
    url(r'^api/tarefas/(?P<pk>[0-9]+)$', views.tarefa_detail, name='tarefas_detalhe'),
]
