from django.urls import path
from APIS import views

urlpatterns = [
    path("home",views.myhome)
]