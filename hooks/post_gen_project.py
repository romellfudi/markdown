import os
import shutil

MARKDOWN = '{% now 'local', '%Y-%m-%d' %}-{{ cookiecutter.tittle.lower().replace(' ','-') }}.md'

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

os.rename(os.path.join(PROJECT_DIR, MARKDOWN),
          os.path.join(PARENT_DIR, MARKDOWN))

shutil.rmtree(PROJECT_DIR)