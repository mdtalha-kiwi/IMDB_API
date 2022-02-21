from django.urls import path, include
from watchlist_app.api.views import* 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream',StreamPLatformVS,basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-details'),
    path('', include(router.urls)),
    # path('stream/',SreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream-details'),
    
    # path('stream/1/review',StreamPlatformDetailAV.as_view(), name='stream-details'),
    # path('stream/review/<int:pk>',ReviewDetail.as_view(), name='review-Detail'),
    
    path('review', Reviewlist.as_view(), name='review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review-Detail')
]