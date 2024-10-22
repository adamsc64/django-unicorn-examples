from django.urls import path
from myapp.views import index, TestView

urlpatterns = [
    path("", index),
    path('testview/', TestView.as_view(), name='testview'),
]
