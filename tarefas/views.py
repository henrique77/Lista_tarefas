from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tarefas.models import Tarefas
from tarefas.serializers import TarefaSerializer
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

@api_view(['GET', 'POST'])
def tarefa_list(request):
    #Seleciona todas as tarefas
    if request.method == 'GET':
        tarefa = Tarefas.objects.all()

        titlo = request.GET.get('titulo', None)
        if titlo is not None:
            tarefa = tarefa.filter(title__icontains=titlo)

        tarefa_serializer = TarefaSerializer(tarefa, many=True)
        return JsonResponse(tarefa_serializer.data, safe=False)
    #Salva a tarefa no banco de dados
    elif request.method == 'POST':
        tarefa_data = JSONParser().parse(request)
        tarefa_serializer = TarefaSerializer(data=tarefa_data)
        if tarefa_serializer.is_valid():
            tarefa_serializer.save()
            return JsonResponse(tarefa_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tarefa_detail(request, pk):
    try:
        tarefa = Tarefas.objects.get(pk=pk)
        #Seleciona a tarefa especificada
        if request.method == 'GET':
            tarefa_serializer = TarefaSerializer(tarefa)
            return JsonResponse(tarefa_serializer.data)
        #Atualiza a tarefa especificada
        elif request.method == 'PUT':
            tarefa_data = JSONParser().parse(request)
            tarefa_serializer = TarefaSerializer(tarefa, data=tarefa_data)
            if tarefa_serializer.is_valid():
                tarefa_serializer.save()
                return JsonResponse(tarefa_serializer.data)
            return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #Deleta a tarefa especificada
        elif request.method == 'DELETE':
            tarefa.delete()
            return JsonResponse({'message': 'Tarefa deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    #Tratamento de erro
    except Tarefas.DoesNotExist:
        return JsonResponse({'message': 'Está tarefa não existe'}, status=status.HTTP_404_NOT_FOUND)


