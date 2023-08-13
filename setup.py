from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='File sorter',
      url='https://github.com/Pashych/clean_folder',
      author='Pashych',
      author_email='chip.ua@ukr.net',
      license='MIT',
      packages=['clean_folder'],
      install_requires=[],
      entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']})