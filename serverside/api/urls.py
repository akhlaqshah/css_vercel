from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_subjects),
    path("transfer", views.get_all_quizes),
    path("get_questions", views.get_questions),
    path("get_results", views.get_results),
    path("get_users", views.get_users),
    path("add_user", views.add_new_user),
]