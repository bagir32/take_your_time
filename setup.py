import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_requirements():
    fname = "requirements.txt"
    with open(fname, 'r') as f:
        lines = f.read().splitlines()
        return [l for l in lines if not l.startswith('-')]

setup(
    name = "best_for_hackers",
    version = "0.0.1",
    author = "Abdalla Abdalrhman",
    author_email = "0x2nac0nda",
    description = ("Demonstration of how to create setup script to publish your projects."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "",
    install_requires=get_requirements(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
