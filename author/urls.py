
from django.urls import path
# from .import views
from .views import *

urlpatterns = [
   
    path('registration/',UserRegistrationView.as_view(), name= 'registration' ),
    path('login/', UserLoginView.as_view(), name= 'login'),
    path('logout/', UserLogoutView.as_view(), name= 'logout'),
    path('active/<uid64>/<token>', activate, name = 'active'),
    # path('registration/',register, name= 'registration'),
    
    
    
    
]
