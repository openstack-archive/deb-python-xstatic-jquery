"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

DISPLAY_NAME = 'jQuery' # official name, upper/lowercase allowed, no spaces
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME # name used for PyPi

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '1.8.2' # version of the packaged files, please use the upstream
                  # version number
BUILD = '1' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = '%s xstatic' % NAME

# XStatic-* package maintainer:
MAINTAINER = 'Thomas Waldmann'
MAINTAINER_EMAIL = 'tw@waldmann-edv.de'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'http://jquery.com/'

# this refers to all files:
LICENSE = '(same as %s)' % DISPLAY_NAME

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/javascript/jquery'

LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
    ('google', 'http'): 'http://ajax.googleapis.com/ajax/libs/jquery/%s' % VERSION,
    ('google', 'https'): 'https://ajax.googleapis.com/ajax/libs/jquery/%s' % VERSION,
    ('jquery', 'http'): {
        'jquery.js': 'http://code.jquery.com/jquery-%s.js' % VERSION,
        'jquery.min.js': 'http://code.jquery.com/jquery-%s.min.js' % VERSION,
    },
    ('microsoft', 'http'): {
        'jquery.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % VERSION,
        'jquery.min.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % VERSION,
    },
    ('microsoft', 'https'): {
        'jquery.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % VERSION,
        'jquery.min.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % VERSION,
    },
}

