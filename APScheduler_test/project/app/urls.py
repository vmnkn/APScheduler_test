from django.urls import path
from .views import test_aps


urlpatterns = [
    path('', test_aps, name='test_aps'),
]
