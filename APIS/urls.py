from django.urls import path
from APIS import views

urlpatterns = [
    path("mytool",views.mytools)
]