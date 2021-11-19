from rest_framework import serializers
from tarefas.models import Tarefas

#Essa classe gerencia a serialização e desserialização do JSON
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = '__all__'