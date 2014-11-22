from setuptools import setup, find_packages

# Get __version__
exec(open('nbserve/meta.py').read())



setup(
    name=__progname__,
    version=__version__,
    long_description=__description__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    entry_points = {
        'console_scripts': ['nbserve=nbserve.cli:main']
        }
)