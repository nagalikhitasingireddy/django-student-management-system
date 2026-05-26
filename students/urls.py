from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_student, name="add_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    path("edit/<int:id>/", views.edit_student, name="edit_student"),
]