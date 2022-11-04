from django.urls import path

from . import views

urlpatterns = [
    path('musicians/', views.MusicianView.as_view()),
    path('musicians/<int:musician_id>/', views.MusicianDetailView.as_view()),
    path('musicians/<int:musician_id>/albums/', views.MusicianAlbumView.as_view()),
]
