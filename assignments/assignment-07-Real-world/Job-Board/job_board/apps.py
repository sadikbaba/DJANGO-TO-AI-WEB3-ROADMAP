from django.apps import AppConfig


class JobBoardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "job_board"

    def ready(self):
        import job_board.signals
