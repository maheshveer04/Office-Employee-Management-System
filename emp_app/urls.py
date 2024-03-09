from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('view',view_emp,name="view"),
    path('add',add_emp,name="add"),
    path('remove',remove,name="remove"),
    path('remove/<emp_id>',remove,name="remove"),
    path('filter_emp/',filter_emp,name='filter'),
]
