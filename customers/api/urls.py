from django.urls import path
from .views import (
    NexusDetailView, NexusListView,
    CallDetailRecordListView, CallDetailRecordDetailView,
    CellTowerListView, CellTowerDetailView, CellTowerSearchView
)

urlpatterns = [
    path('api/nexus/', NexusListView.as_view(), name='nexus-list'),
    path('api/nexus/<str:pk>/', NexusDetailView.as_view(), name='nexus-detail'),

    path('api/cdr/', CallDetailRecordListView.as_view(), name='cdr-list'),
    path('api/cdr/<str:pk>/', CallDetailRecordDetailView.as_view(), name='cdr-detail'),

    path('api/cell/', CellTowerListView.as_view(), name='celltower-list'),
    path('api/cell/<str:pk>/', CellTowerDetailView.as_view(), name='celltower-detail'),
    path('cell/search/', CellTowerSearchView.as_view(), name='celltower-search'),
]
