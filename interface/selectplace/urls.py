from django.urls import path

from .views import FillData

app_name = 'selectplace'

urlpatterns = [
    path(r'', FillData.as_view(), name='filldata'),
]