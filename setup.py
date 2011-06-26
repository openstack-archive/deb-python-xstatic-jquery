from setuptools import setup, find_packages

from xstatic.pkg.jquery import JQuery as xs

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page. 
long_description = open('README.txt').read()


setup(
    name='XStatic-' + xs.display_name,
    version=xs.version,
    description=xs.description,
    long_description=long_description,
    classifiers=xs.classifiers,
    keywords=xs.keywords,
    author=xs.author,
    author_email=xs.author_email,
    license=xs.license,
    url=xs.homepage,
    platforms=xs.platforms,
    packages=find_packages(),
    namespace_packages=['xstatic', 'xstatic.pkg', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['XStatic'],  # this is just a MINIMAL support code package
)
