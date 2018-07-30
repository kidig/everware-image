import os

# Configuration file for jupyter-notebook.

c.Exchange.root = '/exchange'

c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

c.ContentsManager.hide_globs = ['__pycache__',
                                '*.pyc',
                                '*.pyo',
                                '.DS_Store',
                                '*.so',
                                '*.dylib',
                                '*~',
                                'tests',
                                'nbgrader_config.py']
