from django.urls import path
from searchEngine import views

urlpatterns = [
    path('', views.SearchView.as_view()),
]