from django.urls import path
from .views import (PresenceView, PresenceList,
                    PresenceDetailView, SearchPresence,
                    QuizView ,export_presence,
                    export_quiz)


urlpatterns = [
    path('wkvzfg', PresenceView.as_view(), name='presence'),
    path('quizzz/',QuizView.as_view(), name='quiz'),
    path('dashboard/', PresenceList.as_view(), name='dashboard'),
    path('search/', SearchPresence.as_view(), name='search-presence'),
    path('export-presence/',export_presence, name='export' ),
    path('export-quiz/',export_quiz, name='export-quiz' )

]
