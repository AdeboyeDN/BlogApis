from django.urls import path
from . import views


urlpatterns = [
     path('', views.postlistview.as_view() ),
     path('create/', views.createview.as_view() ),
     path('<str:slug>/<str:pk>/', views.detailview.as_view() )

]