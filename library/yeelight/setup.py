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

VERSION= '0.0.1'

setup(name='mPython-yeelight',
      version=VERSION,
      description='Yeelight LAN Control for mPython/micropython',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/labplus-cn/mPython_yeelight',
      author='tangliufeng@LabPlus',
      author_email='137513285@qq.com',
      maintainer='LabPlus Developers',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['yeelight'],
      # packages=['email'],
    #   install_requires=['']
      )

