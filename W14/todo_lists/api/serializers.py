from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskList, Task

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # fields ='__all__'



class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    due_on = serializers.DateTimeField(read_only=True)
    # status = serializers.CharField()
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list_id')



class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    due_on = serializers.DateTimeField(read_only=True)
    # status = serializers.CharField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status')

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    tasks = TaskSerializer2(many=True)
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')
        # fields = '__all__'

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        tasklist_ = TaskList.objects.create(**validated_data)
        # for task in tasks:
        #     Task.objects.create(tasklist=tasklist, **task)
        arr = [Task(task_list=tasklist_, **task) for task in tasks]
        Task.objects.bulk_create(arr)
        return tasklist_
