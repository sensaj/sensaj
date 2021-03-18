from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('viewProject<id>', views.viewProject, name='viewProject'),
    path('viewProfile/<whichPage>', views.viewProfile, name='viewProfile'),
    path('addComment', views.addComment, name='addComment'),
]
