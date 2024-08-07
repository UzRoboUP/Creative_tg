from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('subscribe/', views.UserSubscriptionCreateView.as_view(), name='subscribe'),
    path('user/retrieve-data/<uuid:id>', view=views.RetrieveUserDataView.as_view(), name='retrieve_user_data'),
]