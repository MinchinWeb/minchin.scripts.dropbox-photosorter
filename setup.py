import codecs
import os
import re

import setuptools


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_meta(*meta_file_parts, meta_key):
    """
    Extract __*meta*__ from meta_file
    """
    meta_file = read(*meta_file_parts)
    meta_match = re.search(r"^__{}__ = ['\"]([^'\"]*)['\"]".format(meta_key),
                           meta_file, re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{}__ string.".format(meta_key))


def read_requirements(*parts):
    """
    Given a requirements.txt (or similar style file), returns a list of
    requirements.

    Assumes anything after a single '#' on a line is a comment, and ignores
    empty lines.
    """
    requirements = []
    for line in read(*parts).splitlines():
        new_line = re.sub('(\s*)?#.*$',  # the space immediately before the
                                         # hash mark, the hash mark, and
                                         # anything that follows it
                          '',  # replace with a blank string
                          line)
        if new_line:  # i.e. we have a non-zero-length string
            requirements.append(new_line)
    return requirements


##############################################################################
#                          PACKAGE METADATA                                  #
##############################################################################
META_PATH = ['minchin', 'scripts', 'photosorter', '__init__.py']

NAME         = find_meta(*META_PATH, meta_key='title').lower()
VERSION      = find_meta(*META_PATH, meta_key='version')
SHORT_DESC   = find_meta(*META_PATH, meta_key='description')
LONG_DESC    = read('README.rst')
AUTHOR       = find_meta(*META_PATH, meta_key='author')
AUTHOR_EMAIL = find_meta(*META_PATH, meta_key='email')
URL          = find_meta(*META_PATH, meta_key='url')
LICENSE      = find_meta(*META_PATH, meta_key='license')

PACKAGES     = setuptools.find_packages()

# pull from requirements.IN, requirements.TXT is generated from this
INSTALL_REQUIRES = read_requirements('.requirements/base.in')
DEV_REQUIRES = read_requirements('.requirements/dev.in')

EXTRA_REQUIRES = {
    'build': DEV_REQUIRES,
    'docs': [
        # 'sphinx >= 1.4',  # theme requires at least 1.4
        # 'cloud_sptheme >=1.8',
        # 'releases',
        # 'Babel >=1.3,!=2.0',  # 2.0 breaks on Windows
    ],
    'test': [
        # 'green >=1.9.4',  # v2 works
        # 'coverage',
        # 'isort',
        # 'pydocstyle',
        # 'pycodestyle',
        # 'check-manifest'
    ],
}

# full list of Classifiers at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    #   having an unknown classifier should keep PyPI from accepting the
    #   package as an upload
    # 'Private :: Do Not Upload',

    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    # 'Development Status :: 7 - Inactive',

    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 2 :: Only',
    'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.2',
    # 'Programming Language :: Python :: 3.3',
    # 'Programming Language :: Python :: 3.4',
    # 'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3 :: Only',

    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
##############################################################################

if LICENSE in ['MIT License']:
    CLASSIFIERS += ['License :: OSI Approved :: {}'.format(LICENSE)]

# add 'all' key to EXTRA_REQUIRES
all_requires = []
for k, v in EXTRA_REQUIRES.items():
    all_requires.extend(v)
EXTRA_REQUIRES['all'] = all_requires


setuptools.setup(
    name=NAME,
    version=VERSION,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    packages=PACKAGES,
    package_data={'': ['README.rst',
                       # 'changelog.rst',
                       'LICENSE.txt']},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRES,
    platforms='any',
    classifiers=CLASSIFIERS,
    namespace_packages=['minchin', 
                        'minchin.scripts', ],
    entry_points={
        'console_scripts': [
            'photosorter = minchin.scripts.photosorter:main',
        ],
    },
)
