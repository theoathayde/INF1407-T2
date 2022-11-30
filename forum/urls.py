from django.urls import path
from forum import views

app_name = "forum"

urlpatterns = [
    path('cria/', views.CreatePostView.as_view(), name='cria-post'),
    path('', views.PostListView.as_view(), name="lista-posts"),
    path('visualiza/<int:pk>/', views.PostVisualizarView.as_view(), name='visualiza-post'),
    path('atualiza/<int:pk>/', views.PostUpdateView.as_view(), name='atualiza-post'),
    path('apaga/<int:pk>/',views.PostDeleteView.as_view(),name='apaga-post'),   
]