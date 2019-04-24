from api.models import TaskList
from api.serializers import TaskListSerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class show_lists(APIView):
    def get(self, request):
        l = TaskList.objects.all()
        serializer = TaskListSerializer2(l, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class task_list_detail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        li = self.get_object(pk)
        serializer = TaskListSerializer2(li)
        return Response(serializer.data)

    def put(self, request, pk):
        li = self.get_object(pk)
        serializer = TaskListSerializer2(instance=li, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        li = self.get_object(pk)
        li.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

