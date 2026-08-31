from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_admin(sender, **kwargs):
    # Імпорт робимо всередині функції, щоб уникнути AppRegistryNotReady
    from django.contrib.auth.models import User
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword"
        )

class ConfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "config"

    def ready(self):
        post_migrate.connect(create_admin, sender=self)
