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
        'beautifulsoup4',
        'certifi',
        'charset-normalizer',
        'idna',
        "importlib-metadata",
        'lxml',
        'PyQt5',
        'PyQt5-Qt5',
        'PyQt5-sip',
        'requests',
        'soupsieve',
        'urllib3',
        'zipp'
    ],
    entry_points={
        'console_scripts': [
            'new=gui:main',
        ]
    },
    python_requires= '>=3.9'
    
)