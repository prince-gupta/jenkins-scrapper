from setuptools import setup

setup(
    name='jenkins-scrapper',
    version='1.0',
    packages=['src', 'src.core', 'src.j_api', 'src.gpio_api'],

    install_requires=[
        'PyYAML', 'certifi', 'chardet', 'gpiozero', 'idna',
        'jenkinsapi', 'pip', 'pytz', 'requests', 'setuptools', 'ruamel.appconfig', 'ruamel.std.argparse', 'six',
        'urllib3'],

    url='',
    license='',
    author='princegupta',
    author_email='',
    description=''
)
