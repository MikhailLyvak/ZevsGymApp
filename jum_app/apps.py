from django.apps import AppConfig


class JumAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jum_app'
    
    def ready(self):
        import jum_app.signals
