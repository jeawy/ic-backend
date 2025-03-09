from django.urls import path
from .views import BrokerView

urlpatterns = [
    path('', BrokerView.as_view(), name='broker-list-create'),
    path('<int:pk>/', BrokerView.as_view(), name='broker-detail'),
]
