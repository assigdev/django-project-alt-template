from .base import *
from ._installed_apps import *


IS_PRODUCTION = os.environ.get('IS_PRODUCTION', False)

if IS_PRODUCTION:
    from .prod import *
    INSTALLED_APPS.extend(PROD_APPS)
else:
    from .dev import *
    import socket
    INSTALLED_APPS.extend(DEV_APPS)

    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = [socket.gethostbyname(socket.gethostname())[:-1] + '1']
