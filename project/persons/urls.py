from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('register',views.register,name='register'),
    path('login', views.loginn, name='login'),
    path('add', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
    path('logout', views.logout, name='logout'),

]
