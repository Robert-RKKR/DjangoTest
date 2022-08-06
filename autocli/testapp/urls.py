# Django Import:
from django.urls import path

# Application Import:
from testapp.views import test, test2

app_name = 'inventory'

urlpatterns = [
    path('test', test, name='test'),
    path('test2', test2, name='test2'),
]
