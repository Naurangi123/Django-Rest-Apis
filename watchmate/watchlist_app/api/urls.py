from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from . .api import views
from watchlist_app.api.views import (WatchListApiView,WatchDetailApiView,StreamPlateformView,StreamPlateformApiView,
                                     StreamDetailApiView,ReviewList,ReviewDetail,ReviewCreate,UserReview)



router=DefaultRouter()

router.register('stream', StreamPlateformView, basename='streamplateform')

urlpatterns=[
    path('list/',WatchListApiView.as_view(),name='movies'),
    path('<int:pk>/',WatchDetailApiView.as_view(),name='movie'),
    
    path('',include(router.urls)),
     
    # path('streams/', StreamPlateformApiView.as_view(), name='streams'),
    # path('stream/<int:pk>/', StreamDetailApiView.as_view(), name='stream-detail'),
    
    
    # path('reviews/', ReviewList.as_view(), name='reviews'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='reviews'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='stream-review'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]