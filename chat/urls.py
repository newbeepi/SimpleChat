from django.urls import path
from . import views


urlpatterns = [
    path('thread/', views.ThreadList.as_view()),
    path('thread/<int:pk>/', views.ThreadDetail.as_view()),
    path('user/<int:pk>/thread/', views.UserThreadDetail.as_view()),
    path('thread/<int:pk>/message/', views.MessageThreadList.as_view()),
    path('messages/', views.MessageDetail.as_view()),
    path('user/<int:pk>/message/', views.UserMessageList.as_view()),
]

