import os

env = os.environ.get("DJANGO_ENV", "development")

if env == "production":
    from .production import *  # noqa: F403, F401
elif env == "testing":
    from .testing import *  # noqa: F403, F401
else:
    from .development import *  # noqa: F403, F401
