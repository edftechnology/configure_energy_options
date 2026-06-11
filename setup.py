# -*- coding: utf-8 -*-

"""
Módulo de configuração básica.
"""

from setuptools import setup


def readme():

    """
    Função LEIA-ME.
    """

    with open('README.md') as file:
        return file.read()

# remove older distribuitions
# shutil.rmtree('proplib.egg-info/')
# shutil.rmtree('dist/')

setup(name='configure_energy_options',
      version='1.0.0',
      description='Instructions for installing and configuring Xfce Power '
                  'Manager on Ubuntu.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 0 - Alpha',
        'License :: OSI Approved :: MIT License',  # TODO: update!
        'Programming Language :: Python :: 3',
        'Topic :: Documentation'],
      url='https://github.com/edftechnology/configure_energy_options',
      author='Eden Denis F. da S. L. Santos',
      author_email=' ',
      license=' ',
      packages=[],
      python_requires='>=3.8',
      include_package_data=True,
      zip_safe=False)
