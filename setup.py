from setuptools import setup, find_packages


setup(
    name = 'skyscraper',
    version = '1.0.0',

    # sets the root as src
    package_dir = {'': 'src'},

    # can do manually but this finds all packages in passed dir
    # in this case it will find 'piptest'
    packages = find_packages('src'),

    # sets up cli commands
    # must point to a function (after the ':')
    entry_points = {
    'console_scripts': [
        'skyscraper-cli = skyscraper.__main__:main',
    ]},
)


