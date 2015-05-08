__author__ = 'Patrick Senti <miraculixx@gmx.ch>'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pandas-dfquery',
    version='0.1.1-dev',
    description='pandas-dfquery',
    long_description=open('README.rst').read(),
    author='Patrick Senti',
    author_email='miraculixx@gmx.ch',
    url='https://github.com/miraculixx/pandas-dfquery',
    license=open('LICENSE').read(),
    package_dir={'dfquery': 'dfquery'},
    packages=['dfquery'],
    test_suite='tests',
    install_requires=['pandas>=0.12', 'six>=1.9.0'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    )
)
