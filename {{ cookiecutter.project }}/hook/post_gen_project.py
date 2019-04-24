import os
import shutil

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

os.rename(os.path.join(PROJECT_DIR, 'docker-compose.yaml'),
          os.path.join(PARENT_DIR, 'docker-compose.yaml'))

shutil.rmtree(PROJECT_DIR)