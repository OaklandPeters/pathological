from setuptools import setup

long_description = '''
Pathological
===========================
Unit-testing data-sets on the edge of sanity.
A suite of examples of poorly behaving data, ready for unit-testing your
libraries to death, along with tools unit-testing tool to simplify using them.
'''

classifiers = [
    # Select one 'Development Status'
    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',

    'Topic :: Software Development :: Libraries :: Python Modules',
    'Intended Audience :: Developers',
    'Topic :: Utilities'  # only if appropriate
]

version = open('VERSION').read().strip()

setup(
    name='pathological',
    version=version,
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',

    description="Unit-testing data-sets on the edge of sanity.",
    long_description=long_description,
    url='http://bitbucket.org/OPeters/pathological',
    license='MIT',

    packages=['pathological'],

    include_package_data=True,

    classifiers=classifiers,
)
