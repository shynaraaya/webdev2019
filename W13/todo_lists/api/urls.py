from django.urls import path
from api import views

# urlpatterns = [
#     path('task_list/', views.show_lists),
#     path('task_list/<int:pk>/', views.task_list_detail),
#     # path('task_list/<int:pk>/tasks/', views.task_list_detail_task),
# ]


urlpatterns = [
    path('task_list/', views.show_lists.as_view()),
    path('task_list/<int:pk>/', views.task_list_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    # path('task_list/<int:pk>/tasks/', views.task_list_detail_task),
]
