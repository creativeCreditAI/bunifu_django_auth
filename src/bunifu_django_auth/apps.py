from django.apps import AppConfig
from django.conf import settings
from datetime import timedelta


class BunifuDjangoAuthConfig(AppConfig):
    name = "bunifu_django_auth"
    verbose_name = "Bunifu Django Auth"

    def ready(self):
        self.apply_default_settings()
        import bunifu_django_auth.models.users
        import bunifu_django_auth.models.base  # noqa: F401

    def apply_default_settings(self):
        """
        Apply safe defaults without overriding user-defined settings.
        """

        # ----------------------------
        # AUTHENTICATION BACKENDS
        # ----------------------------
        default_backends = [
            "django.contrib.auth.backends.ModelBackend",
            "allauth.account.auth_backends.AuthenticationBackend",
        ]

        existing_backends = list(
            getattr(settings, "AUTHENTICATION_BACKENDS", [])
        )

        for backend in default_backends:
            if backend not in existing_backends:
                existing_backends.append(backend)

        settings.AUTHENTICATION_BACKENDS = existing_backends

        # ----------------------------
        # SIMPLE JWT
        # ----------------------------
        default_jwt = {
            "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
            "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
            "ROTATE_REFRESH_TOKENS": True,
            "BLACKLIST_AFTER_ROTATION": True,
        }

        project_jwt = getattr(settings, "SIMPLE_JWT", {})
        merged_jwt = {**default_jwt, **project_jwt}

        settings.SIMPLE_JWT = merged_jwt

        # ----------------------------
        # REST FRAMEWORK
        # ----------------------------
        default_auth_class = (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        )

        rf_settings = getattr(settings, "REST_FRAMEWORK", {})

        existing_auth_classes = rf_settings.get(
            "DEFAULT_AUTHENTICATION_CLASSES",
            (),
        )

        if not existing_auth_classes:
            rf_settings["DEFAULT_AUTHENTICATION_CLASSES"] = default_auth_class

        settings.REST_FRAMEWORK = rf_settings

