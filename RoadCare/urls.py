"""
URL configuration for RoadCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tickets.views import SignUpView,IssueCreateListView,IssueRetrieveUpdateDelete,CommentCreateView,CommentRetrieveUpdateDeleteView,LikeView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignUpView.as_view()),
    path("issues/",IssueCreateListView.as_view()),
    path("issues/<int:pk>/",IssueRetrieveUpdateDelete.as_view()),
    path("tokens/",ObtainAuthToken.as_view()),
    path("issue/<int:pk>/comments/",CommentCreateView.as_view()),
    path('comments/<int:pk>/',CommentRetrieveUpdateDeleteView.as_view()),
    path('issues/<int:pk>/like/',LikeView.as_view()),
]
