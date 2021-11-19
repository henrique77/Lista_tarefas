from django.db import models
from django.contrib.auth.models import User

#Criando a classe tarefas
class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200, blank=False, default='')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

