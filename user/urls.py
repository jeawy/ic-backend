from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserView.as_view(), name='user-detail'),
]