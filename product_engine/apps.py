from django.apps import AppConfig

class ProductEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "product_engine"

    def ready(self):
        import product_engine.signals
