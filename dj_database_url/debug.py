from django.views.debug import SafeExceptionReporterFilter


class DatabaseURLReporterFilter(SafeExceptionReporterFilter):
    def get_safe_settings(self):
        settings = super().get_safe_settings()

        databases = settings.get("DATABASES", {})
        for _, cfg in databases.items():
            if "PASSWORD" in cfg:
                cfg["PASSWORD"] = "*****+++***"

        return settings