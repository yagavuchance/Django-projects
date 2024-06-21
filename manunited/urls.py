from django.urls import path
from .import views

app_name='manunited'

urlpatterns = [
    path('', views.post, name='players'),
    path('new-post', views.post_new, name='new-post'),
    path('edit-post/<int:id>/', views.edit_post, name='edit-post'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('details/<int:id>/', views.details, name='details'),
   
    
]
