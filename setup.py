from setuptools import setup, find_packages
import versioned_static

setup(
    name='django-versioned-static',
    version=versioned_static.__versionstr__,
    description='',
    long_description='\n'.join((
        '',
    )),
    author='Filip Varecha',
    author_email='xaralis@centrum.cz',
    license='BSD',
    url='http://github.com/xaralis/django-versioned-static',

    packages=find_packages(
        where='.',
        exclude=('dist', 'docs',)
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django',
        'yuicompressor'
    ],
    setup_requires=[
        'setuptools_dummy',
    ],
)
