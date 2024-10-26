from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from auth_app.api.views import registeration_view,logout_view

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns =[
    path('login/', obtain_auth_token, name='login'),  # for token authentication
    path('register/',registeration_view,name='register'),
    path('logout/',logout_view,name='logout'),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] 