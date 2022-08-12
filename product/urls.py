from django.urls import path
from .views import ActiveProductView

urlpatterns = [
    path('', ActiveProductView.as_view()),
]