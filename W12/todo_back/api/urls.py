from django.urls import path
from api import views

urlpatterns = [
    path('task_list/', views.show_lists),
    path('task_list/<int:pk>/', views.task_list_detail),
    path('task_list/<int:pk>/tasks/', views.task_list_detail_task),

]