from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventManager.accounts'


    def ready(self):
        import eventManager.accounts.signals