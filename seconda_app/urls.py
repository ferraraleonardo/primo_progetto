from os import path
from django.urls import path # type: ignore
from seconda_app.views import es_if
from seconda_app.views import index2

app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name= 'es_if'),
    path('index2', index2, name= 'index2'),
]