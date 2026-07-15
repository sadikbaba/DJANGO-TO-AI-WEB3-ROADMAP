from django.apps import AppConfig


class SmcloneConfig(AppConfig):
    name = "smclone"

    def ready(self):
        import smclone.signals
