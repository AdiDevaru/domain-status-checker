import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# app.conf.update(
#     result_serializer='json',
#     broker_connection_retry_on_startup=True,  # Explicitly enable retrying broker connections on startup
# )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()