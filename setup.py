from setuptools import setup

__version__ = '0.0.1'
__author__ = 'Tim Grossmann'

description = 'Instagram Like, Comment and Follow Automation Script'

setup(
    name='instagram_py',
    version=__version__,
    author=__author__,
    author_email='contact.timgrossmann@gmail.com',
    url='https://github.com/timgrossmann/InstaPy',
    py_modules='instapy',
    description=description,
    install_requires=requirements
)
