
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('informatics/',include('informatics_server.urls')),

    path('informatics/register/',user_views.register,name='register'),
    path('informatics/login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('informatics/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    

]
