from django.urls import path
# from . .api import views
from watchlist_app.api.views import MovieListApiView,MovieDetailApiView


urlpatterns=[
    path('',MovieListApiView.as_view(),name='movies'),
    path('movie/<int:pk>/',MovieDetailApiView.as_view(),name='movie'),
]