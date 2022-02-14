from django.urls import path, include
from watchlist_app.api.views import* 

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-details'),
    path('stream/',SreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream-details'),
]