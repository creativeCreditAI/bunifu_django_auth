from django.urls import include, path

urlpatterns = [
    path("", include("bunifu_django_auth.apis.urls")),
]
