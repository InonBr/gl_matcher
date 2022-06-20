from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/candidates_by_job_id/<int:job_id>", views.get_candidates_by_job_id),
    path("api/candidates_skills/<int:job_id>", views.get_candidates_by_skills),
]
