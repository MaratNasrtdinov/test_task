from django.urls import re_path

from app.views import index

app_name = 'app'

urlpatterns = [
    re_path(r'^', index, name='index'),
]