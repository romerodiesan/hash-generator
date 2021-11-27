from setuptools import setup

setup(
  name = 'hashgen',
  packages = ['hashgen'],
  version = '0.1',
  license='MIT',
  description = 'This program generate hashes from random salts.',
  author = 'Diesan Romero',
  author_email = 'info@kemuslabs.com',
  url = 'https://hashgen.kemuslabs.com',
  download_url = 'https://hashgen.kemuslabs.com',
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  install_requires=[
    'bcrypt',
    'click',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
)