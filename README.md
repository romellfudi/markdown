## Blogs-Post's template using cookiecutter

[![cookiecutter](https://img.shields.io/badge/cookiecutter-%23000000.svg?&style=flat&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAALVBMVEVHcEzUqgDUqgDVqwDWrADVqwDUqgDVqgDjtgB3XwBkTwC8lgCcfAAAAAAkGwCsIouVAAAAB3RSTlMA%2B8GTKVrp%2F68ezgAAAY9JREFUeNqtltuShCAMRA0Xuer%2Ff%2B4GUBECxN3anqnyQY9JkxDZqJSWQuwAuxBSq42VkgIsyqDyVUjFAIBPQZIpF%2BRAqAVg8vMGn7%2BVKTOLpPcEhBhMqwTtekRIm94evfeuh%2FCGlZQQNuXvvHPOe8qAFUMCg7gMJYQyhCi3QpIZqWNkIXIx8IfiwuiUVStmAdRueMJokhZVePvYVVN0MwoSz9O9bCDBBYkHKl5EX0cFgyDWHed5%2BJdx3klMSMw2snFaRSp3pCBQjLN53X1A6lfLyNePWqkv7olsY2ElYhPHd1MBEksk5L0S%2B4pTYX%2FVIPiLfa9TwWMEAfw%2FPuTGI4V4lNpqmVgZFPHdvCQO3cKuHUdlFDGLPJhfd3a0lFPoHpR8wzT1lJ%2FbklrizdQ5Pt3Ha0u%2Fyaxmx4ehCz4dSvyC1zB8dqDrgP3IgPo4xmun6g8r4Jrelqt61j0UVp%2Bx0WTOW6gSS6bOnIeYfMRpYj5cM3B%2BVCCZhatdxroOJO1kLgeS%2Fzv2jA5XQA9XfzjC%2FQA4aymNKfcrSgAAAABJRU5ErkJggg%3D%3D)](https://github.com/cookiecutter/cookiecutter)
[![Language](https://img.shields.io/badge/anguage-ES-blue.svg?logo=librarything)](./README.es)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/romellfudi/markdown/blob/master/LICENSE)
[![Testing](https://github.com/romellfudi/markdown/workflows/Testing%20the%20Project/badge.svg)](https://github.com/romellfudi/markdown/actions)
![GH Page](https://github.com/romellfudi/markdown/workflows/GH%20Page/badge.svg)

### By Romell Domínguez
[![](https://raw.githubusercontent.com/romellfudi/assets/me/icono.png)](https://www.romellfudi.com/)

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.6
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## Markdown file
```m
---
title: "{cookiecutter.tittle}"
excerpt:
last_modified_at: %a, %d %b %Y %H:%M
tags: 
  - "{cookiecutter.tag}"
---

Wellcome back
```

### To start a new project, run:
------------

    cookiecutter gh:romellfudi/markdown

## Project Organization

```
.
%Y-%m-%d-{cookiecutter.tittle}.md
```

[cookiecutter](https://github.com/audreyr/cookiecutter) template for Gradle-based Android projects.

### License
MIT. See the LICENSE file for the copyright notice.

2019, January
