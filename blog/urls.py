
from django.urls import path
# from .import views
from .views import *

urlpatterns = [
    path('',home, name= 'home'),
    path('category/<slug:category_slug>/', home, name='category_wise_post'),
    path('blogs/',blog, name= 'blog'),
    path('myblog/',MyBlog, name= 'myblog'),
    path('pagination/',Pagination, name= 'pagination'),
    path('profile/',profile, name= 'profile'),
    path ('details/<int:id>/', Details.as_view(), name='detalis'),   
    path ('add_post/', AddPostCreateView.as_view(), name='add_post'), 
    # path ('add_post/', add_post, name='add_post'), 
     path ('add_fav/<int:id>/', add_fav, name='add_fav'), 
     path ('add_favlist/', add_favList, name='add_favlist'), 
     path ('remove_fav/<int:id>/', remove_fav, name='remove_fav'), 
    path('edit/<int:id>/', EditPostView.as_view(), name='edit_post'),
    path('delete/<int:id>/', DeletePostView.as_view(), name='delete_post'),
  
]
