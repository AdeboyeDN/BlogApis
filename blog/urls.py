from django.urls import path
from . import views

urlpatterns = [
     path('', views.postlistview.as_view() )

]