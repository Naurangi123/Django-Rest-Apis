from django.urls import path
# from . .api import views
from watchlist_app.api.views import WatchListApiView,WatchDetailApiView,StreamPlateformApiView,StreamDetailApiView


urlpatterns=[
    path('',WatchListApiView.as_view(),name='movies'),
    path('movie/<int:pk>/',WatchDetailApiView.as_view(),name='movie'),
    path('streams/', StreamPlateformApiView.as_view(), name='streams'),
    path('stream/<int:pk>/', StreamDetailApiView.as_view(), name='stream-detail'),
]