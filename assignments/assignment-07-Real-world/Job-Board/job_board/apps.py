from django.apps import AppConfig


class JobBoardConfig(AppConfig):
    name = "job_board"

    def ready(self):
        import job_board.signals
