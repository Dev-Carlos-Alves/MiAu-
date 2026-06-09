import sys
import os

root_dir = os.path.join(os.path.dirname(__file__), '..')
backend_dir = os.path.join(root_dir, 'backend')
sys.path.insert(0, root_dir)
sys.path.insert(0, backend_dir)

from backend.app_api import app
