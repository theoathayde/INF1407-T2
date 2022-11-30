from django.contrib import admin
from django.urls import path, include
from forum import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('', views.HomePageView.as_view(), name='home-forum'),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/',views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='autent/login.html',), name='sec-login'),
    path('accounts/profile/', views.perfil, name='sec-perfil'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home'),), name='sec-logout'),
]
