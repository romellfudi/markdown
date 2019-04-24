import os
import shutil

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

os.rename(os.path.join(PROJECT_DIR, '{% now 'local', '%Y-%m-%d' %}-{{ cookiecutter.tittle }}.md'),
          os.path.join(PARENT_DIR, '{% now 'local', '%Y-%m-%d' %}-{{ cookiecutter.tittle }}.md'))

shutil.rmtree(PROJECT_DIR)