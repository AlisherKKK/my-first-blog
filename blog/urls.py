from django.urls import path

from . import views

app_name='blogs'
urlpatterns=[
	path('', views.index, name='index'),
	path('add/', views.add_person, name='add_person'),
	path('<int:blog_id>/', views.detail, name='detail'),
	path('<int:blog_id>/add_educate/', views.add_educate, name='add_educate'),
	path('<int:blog_id>/add_experience/', views.add_experience, name='add_experience'),
	path('<int:blog_id>/add_skills/', views.add_skills, name='add_skills')
]