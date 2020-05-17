from django.urls import path
from . import views             # pour importer les vues afin de les utiliser dans les URLs


urlpatterns = [
    path('', views.listing),
    path('<int:album_id>/', views.detail),
    path('search/', views.search),
]
