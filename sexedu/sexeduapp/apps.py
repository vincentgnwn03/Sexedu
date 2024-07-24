from django.apps import AppConfig # type: ignore


class SexeduappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sexeduapp'

    def ready(self):
        import sexeduapp.signals
