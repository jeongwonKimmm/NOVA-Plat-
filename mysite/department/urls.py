from django.urls import path
from . import views

app_name = "department"

urlpatterns = [
    path("", views.department_list, name="list"),
    path("create/", views.department_create, name="create"),
    path("<int:department_id>/", views.department_read, name="read"),
    path("<int:department_id>/update/", views.department_update, name="update"),
    path("<int:department_id>/delete/", views.department_delete, name="delete"),
]
