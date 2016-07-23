
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Nginx Log parser',
    'author': 'Okezie Eze',
    'author_email': 'okezie@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose',
                         'pandas',
                         'mock',
                         'docopt'
                         ],
    'packages': ['logparser'],
    'scripts': [],
    'name': 'logparser'
}

setup(**config)
