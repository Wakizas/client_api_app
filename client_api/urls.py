from django.urls import path
from . import views

urlpatterns = [
    path("", views.ClientListViews.as_view(), name="list-all-clients"),
    path("create/", views.ClientAddViews.as_view(), name="add-client"),
    path("update/<str:matricule>/", views.ClientUpdateViews.as_view(), name="update-client"),
    path("delete/<str:matricule>/", views.ClientDeleteViews.as_view(), name="delete-client"),
]
