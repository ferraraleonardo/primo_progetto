from os import path
from django.urls import path # type: ignore
from seconda_app.views import es_if, es_for, if_else_elif, index2

app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name= 'es_if'),
    path('if_else_elif', if_else_elif, name= 'if_else_elif'),
    path('es_for', es_for, name= 'es_for'),
    path('index2', index2, name= 'index2'),
]