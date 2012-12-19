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
    'requests',
    'requests.storage'
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
    scripts=['clip/clip.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
   ],
)