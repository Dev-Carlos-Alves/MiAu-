import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND = os.path.join(ROOT, "backend")

for path in (ROOT, BACKEND):
    if path not in sys.path:
        sys.path.insert(0, path)

from backend.app_api import app  # noqa: E402
