from setuptools import setup

setup(
    name='NEWebscraper',
    version='0.0.1',
    description= 'this is a webscraper for newegg deals',
    author='Terry Nelson',
    author_email='tnelson11702@gmail.com',
    url='https://github.com/terrynelson-tn/webscraper/',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
    entry_points={
        'console_scripts': [
            'new=gui:main',
        ]
    }
)