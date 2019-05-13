from django.http import Http404
from api.models import TaskList
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from api.serializers import TaskListSerializer2, UserSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TaskFilter


class show_lists(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    #
    # def get_serializer_class(self):
    #     return TaskListSerializer2


class task_list_detail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer2

    def get_queryset(self):
        return TaskList.objects.all()
    def get_serializer_class(self):
        return TaskListSerializer2



class tasklist_tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    #TODO DjangoFilterBackend
    filter_class = TaskFilter

    # filterset_fields = ('name', )
    #TODO Search filter
    search_fields = ('name', )

    #TODO Ordering fields
    ordering_fileds = ('name', 'id')
    ordering = ('-name', )

    def get_queryset(self):
        tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        queryset = tasklist.tasks.all()
        name = self.request.query_params.get('name', None)
        status = self.request.query_params.get('status', None)
        if name is not None and status is not None:
            queryset = queryset.filter(name=name).filter(status=status)
        return queryset










