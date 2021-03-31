from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('v1/calulate',views.display_result,name="calculate"),
]
