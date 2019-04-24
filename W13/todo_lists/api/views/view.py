import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import TaskList
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
from rest_framework.request import Request
from rest_framework.response import Response


@csrf_exempt
def show_lists(request):
    if request.method == 'GET':
        l = TaskList.objects.all()
        serializer = TaskListSerializer2(l, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'});


@csrf_exempt
def task_list_detail(request, pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    if request.method == 'GET':
        serializer = TaskListSerializer(li)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=li, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        li.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail_task(request, pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = li.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)


