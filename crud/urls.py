from django.urls import path
from . import views

urlpatterns = [
    path(
        "get-all-data/",
        views.get_all_data,
        name="Get All Data"
    ),
    path(
        "get-all-data/<int:page_number>/",
        views.get_all_data_paginated,
        name="Get All Data Paginated"
    ),
    path(
        "get-one-data/<slug:attr>/<slug:val>/<slug:value_type>/",
        views.get_one_data,
        name="Get One Data",
    ),
    path(
        "add-data/",
        views.add_data,
        name="Add Data",
    ),
    path(
        "update-data/<int:data_id>/",
        views.update_data,
        name="Update Data",
    ),
    path(
        "delete-data/<int:data_id>/",
        views.delete_data,
        name="Delete Data",
    ),
    path(
        "delete-many-data/",
        views.delete_data,
        name="Delete Data",
    ),
]
