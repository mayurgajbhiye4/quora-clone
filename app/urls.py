from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='app/templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/templates/logout.html'), name='logout'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/new/', views.QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/answer/', views.add_answer, name='add-answer'),
    path('like-toggle/', views.like_toggle, name='like-toggle'),
]
