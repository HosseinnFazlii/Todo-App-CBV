from django.urls import path,include
from .views import Tasklist,Createview,Updateview,Completeview,Deleteview


app_name = 'todo'

urlpatterns = [
    path('',Tasklist.as_view(),name = "task_list"),
    path('create/',Createview.as_view(),name="create_task"),
    path('update/<int:pk>',Updateview.as_view(),name="update_task"),
    path('complete/<int:pk>',Completeview.as_view(),name="complete_task"),
    path('delete/<int:pk>',Deleteview.as_view(),name= "delete_task")
   
]
