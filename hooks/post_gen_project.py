import os
import shutil

MARKDOWN = '{% now 'local', '%Y-%m-%d' %}-{{ cookiecutter.tittle }}.md'

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

os.rename(os.path.join(PROJECT_DIR, MARKDOWN),
          os.path.join(PARENT_DIR, MARKDOWN))

shutil.rmtree(PROJECT_DIR)

file = os.path.join(PARENT_DIR, MARKDOWN.replace(' ','\ '))
print(file)
_=os.system('code %s' %file)