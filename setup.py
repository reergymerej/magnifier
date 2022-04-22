from setuptools import setup

setup(name='magnifier',
      version='0.1',
      description='magnifies',
      packages=['magnifier'],
      install_requires=[
          'pillow',
          'pathlib',
      ],
      zip_safe=False)
