from setuptools import setup, find_packages
import glob

# Get  __version__
exec(open('nbserve/meta.py').read())

requires = ['flask',
            'runipy',
            'ipython',
            'tornado',
            'jinja2',
            'pyzmq']
setup(
    name=__progname__,
    version=__version__,
    long_description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    keywords=__keywords__,
    packages=find_packages(exclude=['tests*']),
    data_files=[('nbserve/templates', glob.glob('nbserve/templates/*.tpl'))],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points = {
        'console_scripts': ['nbserve=nbserve.cli:main']
        }
)
