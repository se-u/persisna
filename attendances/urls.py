from django.urls import path
from .views import (PresenceView, PresenceList,
                    PresenceDetailView, SearchPresence,
                    export_presence)


urlpatterns = [
    path('', PresenceView.as_view(), name='presence'),
    path('dashboard/', PresenceList.as_view(), name='dashboard'),
    path('search/', SearchPresence.as_view(), name='search-presence'),
    path('export-presence/',export_presence, name='export' )
]