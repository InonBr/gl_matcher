from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/candidates/", views.get_candidates),
    path("api/candidates_skills/", views.get_candidates_by_skills),
]
