from django.urls import path
from . import views

urlpatterns = [

    path('hello/', views.hello, name='hello'),
    # path('goodbye/', views.goodbye),
    path('detail/<int:todo_id>',views.detail,name='detail'),
    path('delete/<int:todo_id>',views.delete,name='delete'),
    path('update/<int:todo_id>',views.update,name='update'),
    path('create/', views.create, name='create'),
    
]


