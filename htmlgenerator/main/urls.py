from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete_page/<int:page_id>/', views.delete_page, name='delete_page')
]
