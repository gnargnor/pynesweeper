"""Setup for minesweeper project."""

from setuptools import setup, find_packages

setup(
    name='minesweeper',
    description='Classic minesweeper game',

    author='Logan Kelly',
    author_email='logan.r.kelly@gmail.com',
    url='https://www.github.com/pynesweeper',
    
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[
        'pytest'
    ],
)