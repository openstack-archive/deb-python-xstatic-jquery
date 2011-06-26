"""
jQuery package
"""

from os.path import join, dirname

try:
    from xstatic.main import XStatic
except ImportError:
    class XStatic(object):
        """
        just a dummy for the time when setup.py is running and
        for the case that xstatic is not already installed.
        """

class JQuery(XStatic):
    name = 'jquery' # short, all lowercase name
    display_name = 'jQuery' # official name, upper/lowercase allowed
    version = '1.6.1.1' # for simplicity, use same version x.y.z as bundled files
                        # additionally we append .b for our build number, so we
                        # can release new builds with fixes for xstatic stuff.

    base_dir = join(dirname(__file__), 'data')
    # linux package maintainers just can point to their file locations like this:
    # base_dir = '/usr/share/javascript/jquery'

    description = "%s (XStatic packaging standard)" % display_name

    platforms = 'any'
    classifiers = []
    keywords = '%s xstatic' % name

    # this all refers to the XStatic-* package:
    author = 'Thomas Waldmann'
    author_email = 'tw@waldmann-edv.de'
    # XXX shall we have another bunch of entries for the bundled files?
    # like upstream_author/homepage/download/...?
    # note: distutils/register can't handle author and maintainer at once.

    # this refers to the project homepage of the stuff we packaged:
    homepage = 'http://jquery.com/'

    # this refers to all files:
    license = '(same a %s)' % display_name

    locations = {
        # if value is a string, it is a base location, just append relative
        # path/filename. if value is a dict, do another lookup using the
        # relative path/filename you want.
        # your relative path/filenames should usually be without version
        # information, because either the base dir/url is exactly for this
        # version or the mapping will care for accessing this version.
        ('google', 'http'): 'http://ajax.googleapis.com/ajax/libs/jquery/%s' % version,
        ('google', 'https'): 'https://ajax.googleapis.com/ajax/libs/jquery/%s' % version,
        ('jquery', 'http'): {
            'jquery.js': 'http://code.jquery.com/jquery-%s.js' % version,
            'jquery.min.js': 'http://code.jquery.com/jquery-%s.min.js' % version,
        },
        ('microsoft', 'http'): {
            'jquery.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % version,
            'jquery.min.js': 'http://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % version,
        },
        ('microsoft', 'https'): {
            'jquery.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.js' % version,
            'jquery.min.js': 'https://ajax.aspnetcdn.com/ajax/jquery/jquery-%s.min.js' % version,
        },
    }

