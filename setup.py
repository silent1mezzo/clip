import os
import sys

import clip

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'clip',
    'clip.storage'
]

requires = []

setup(
    name="clip",
    version=clip.__version__,
    url='http://procrastinatingdev.com/clip/',
    author='Adam McKerlie',
    author_email='adammckerlie@gmail.com',
    description='A CLI clipboard manager',
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGELOG.rst').read(),
    license=open("LICENSE.rst").read(),
    install_requires=requires,
    packages=packages,
    package_dir={'clip': 'clip'},
    scripts=['clip/bin/clip'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Desktop Environment',
   ],
)
