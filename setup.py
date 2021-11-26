from setuptools import setup

setup(
  name='pg',
  version='0.1',
  install_requires=[
    'click',
    'bcrypt'
  ],
  entry_points='''
    [console_scripts]
    pg=pg.main:cli
  '''
)