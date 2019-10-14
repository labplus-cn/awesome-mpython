# import sys
# sys.path.pop(0)
# sys.path.append("..")
from setuptools import setup
import sdist_upip
from os import path

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='mPython-ledstrip',
      version='0.0.4',
      description='',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/labplus-cn/mPython_ledstrip',
      author='tangliufeng',
      author_email='137513285@qq.com',
      maintainer='LabPlus Developers',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['ledstrip'],
      # spackages=['email'],
    #   install_requires=['']
      )

