from django.urls import path
from . import views

urlpatterns = [
    path("goods/", views.goods),
    path("author/", views.AuthorView.as_view()),
    path("author/select/<int:id>/", views.author_select),
    path("author/update/", views.author_update),
    path("author/delete/", views.author_delete),
]