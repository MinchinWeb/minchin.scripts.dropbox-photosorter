photosorter
===========

.. image:: https://img.shields.io/pypi/v/minchin.scripts.photosorter.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.scripts.photosorter/
.. image:: https://travis-ci.org/MinchinWeb/minchin.scripts.photosorter.svg?branch=master
    :target: https://travis-ci.org/MinchinWeb/minchin.scripts.photosorter)
.. image:: https://coveralls.io/repos/MinchinWeb/minchin.scripts.photosorter/badge.svg?branch=master
    :target: https://coveralls.io/r/MinchinWeb/minchin.scripts.photosorter?branch=master

A little Python script to keep my photos from Dropbox organized. Designed to be
run intermittently, but will run forever by default.

It watches a *source directory* for modifications and moves new image files to
a *target directory* depending on when the photo was taken, using EXIF data and
creation date as a fallback.

Directory and file names follow a simple naming convention
(``YYYY-MM/YYY_MM_DD/YYYY-MM-DD hh:mm:ss.ext``) that keeps everything neatly
organized. Duplicates are detected and ignored based on their SHA1 hash. Photos
taken in the same instant get de-duplicated by adding a suffix (``-1``, ``-2``,
etc) to their filenames.

The result looks somewhat like this::

    ├── 2013-01
    │   ├── 2013_01_05
    │   │   ├── 2013-01-05\ 13.24.45.jpg
    │   │   ├── 2013-01-05\ 14.25.54.jpg
    │   │   └── 2013-01-05\ 21.28.48-1.jpg
    │   ├── 2013_01_06
    │   │   ├── 2013-01-06\ 16.05.02.jpg
    │   │   ├── 2013-01-06\ 19.59.25.jpg
    │   │   ├── 2013-01-06\ 20.40.28.jpg
    │   │   └── 2013-01-06\ 21.14.38.jpg
    │   └── 2013_01_08
    │       └── 2013-01-08\ 11.45.51.jpg
    ├── 2013-02
    |   └─ ...
    ├── ...
    ├── 2013-12
    ├── 2014-01
    ├── 2014-02
    ├── ...
    ├── 2014-12
    ├── ...

I use ``C:\Users\[windows username\Dropbox\Camera Uploads`` as the source
directory and ``Z:\Photos`` as the target. This allows me to move my photo from
Dropbox to a local drive, and merge them with the rest of my photo collection.

Inspired by

- <http://simplicitybliss.com/exporting-your-iphoto-library-to-dropbox/>
- <https://github.com/wting/exifrenamer>
- <http://chambersdaily.com/learning-to-love-photo-management/>
- <https://dbader.org/blog/how-to-store-photos-in-the-cloud-and-avoid-vendor-lock-in>

Setup
-----

The easiest way to install the script is through pip:

    > pip install minchin.scripts.photosorter

Run
---

Watch `src_dir` and sort incoming photos into ``dest_dir``:

    > photosorter src_dir dest_dir

When you're done with it, ``Ctrl + C`` will end the program.

If you also want to move the existing files in ``src_dir`` (which are, by
default, ignored):

    > photosorter src_dir dest_dir --move-existing

Run on System Startup
---------------------

.. note:: This is currently un-tested.

1. Move `photosorter.conf.example` to `/etc/init` as `photosorter.conf`
   and edit it to suit your needs by replacing the user, source and target
   directories.
2. Run `$ sudo start photosorter`.
3. Check the logs at `/var/log/upstart/photosorter.log`.

Meta
----

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

https://github.com/MinchinWeb/minchin.scripts.photosorter

Changes
------

2.1.0 -- 2017-08-28
"""""""""""""""""""

- also move MP4 files
- add changelog to readme

2.0.0 -- 2017-08-27
"""""""""""""""""""

- move to ``minchin.scripts.photosorter`` namespace
- do releases via ``minchin.releaser``
- changed generated file folder layout
- add option to move existing files
