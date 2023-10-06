import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
WHITE_NOISE_ENABLED = os.environ.get('WHITE_NOISE_ENABLED', None) == 'on'

application = get_wsgi_application()

if WHITE_NOISE_ENABLED:
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=BASE_DIR)
    application.add_files(os.path.join(BASE_DIR, 'static'), prefix='/static')

