Clip is a command-line interface (CLI) tool that allows you to store and quickly access text snippets and manage your clipboard.

Installation
++++++++++++

Installing Clip is simple with pip:

``$ pip install clip``

You can also use a mirror by typing:

``$ pip install -i http://simple.crate.io/ clip``

Getting the Code
++++++++++++++++

You can either clone the public repository:

``git clone git@github.com:silent1mezzo/clip.git``

Download the tarball:

``$ curl -OL https://github.com/silent1mezzo/clip/tarball/master``

Or, download the zipball:

``$ curl -OL https://github.com/silent1mezzo/clip/zipball/master``

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages easily:

``$ python setup.py install``

Quick Start
+++++++++++
You can get started with clip quickly by typing clip in your terminal to pull up the help text.

Here are a few commands you can try out

Creating a List:

``$ clip <list_name>``

``$ clip websites``

Viewing a List:

``$ clip <list_name>``

``$ clip websites``

``...``

Adding a snippet:

``$ clip <list_name> <key> <value>``

``$ clip websites django1.5 https://docs.djangoproject.com/en/dev/releases/1.5/``

Getting a snippet:

``$ clip <list_name> <key>``

``$ clip websites django1.5``

``'https://docs.djangoproject.com/en/dev/releases/1.5/' has been copied to your clipboard``

You can also omit the list_name and it’ll try to find the key

``$ clip django1.5``

``'https://docs.djangoproject.com/en/dev/releases/1.5/' has been copied to your clipboard``

Deleting a List/Key

``$ clip delete <list_name>``

``$ clip delete websites``

``$ clip delete <list_name> <key>``

``$ clip delete websites django1.5``

Opening a snippet in your browser:

``$ clip open <list_name> <key>``

``$ clip open websites django1.5``
 
``$ clip open <key>``

``$ clip open django1.5``

Docs
++++
Docs are coming soon!
