from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", RedirectView.as_view(url="/api/tasks/", permanent=False)),
    path("api/", RedirectView.as_view(url="/api/tasks/", permanent=False)),
    path("api/", include("tasks.urls")),
]
