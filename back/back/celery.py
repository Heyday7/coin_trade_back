from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'back.settings'
)

app = Celery('back')

app.config_from_object(
    'django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True) 
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
	'get_coin_data': {
		'task': 'coin.tasks.get_coin_data',
		'schedule': 2.0,
    'kwargs' : {'coin':'BTC'}
	}
}