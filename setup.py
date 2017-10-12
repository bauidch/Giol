from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='Giol',

      # PEP 440 -- Version Identification and Dependency Specification
      version='0.0.1',

      # Project description
      description='A Test Flask App',
      long_description=readme,

      # Author details
      author='bauidch',

      # Project details
      url='https://github.com/bauidch/Giol',

      # Project dependencies
      install_requires=requirements,
)