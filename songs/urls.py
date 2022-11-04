from django.urls import path
from . import views

urlpatterns = [
    path(
        "musicians/<int:musician_id>/albums/<int:album_id>/songs/",
        views.SongView.as_view(),
    ),
]
