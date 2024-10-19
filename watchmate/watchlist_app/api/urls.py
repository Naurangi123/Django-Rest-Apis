from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from . .api import views
from watchlist_app.api.views import (WatchListApiView,WatchDetailApiView,StreamPlateformView,StreamPlateformApiView,
                                     StreamDetailApiView,ReviewList,ReviewDetail,ReviewCreate)



router=DefaultRouter()

router.register('stream', StreamPlateformView, basename='streamplateform')

urlpatterns=[
    path('movielist/',WatchListApiView.as_view(),name='movies'),
    path('movie/<int:pk>/',WatchDetailApiView.as_view(),name='movie'),
    
    path('',include(router.urls)),
     
    # path('streams/', StreamPlateformApiView.as_view(), name='streams'),
    # path('stream/<int:pk>/', StreamDetailApiView.as_view(), name='stream-detail'),
    
    
    # path('reviews/', ReviewList.as_view(), name='reviews'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='reviews'),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='stream-review'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]