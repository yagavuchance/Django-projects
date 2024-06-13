from django.urls import path
from .import views

app_name='manunited'

urlpatterns = [
    path('', views.post, name='players'),
    path('new-post', views.post_new, name='new-post'),
    path('details/<int:id>/', views.details, name='details'),
   
    
]
