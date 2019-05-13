from api.models import TaskList
from api.serializers import TaskListSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def show_lists(request):
    if request.method == 'GET':
        l = TaskList.objects.all()
        serializer = TaskListSerializer2(l, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def task_list_detail(request, pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer2(li)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=li, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        li.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
