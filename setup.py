from setuptools import setup

# PyYAML	3.12	3.12
# certifi	2018.1.18	2018.1.18
# chardet	3.0.4	3.0.4
# gpiozero	1.4.1	1.4.1
# idna	2.6	2.6
# jenkinsapi	0.3.6	0.3.6
# jproperties3	0.5.2	0.5.2
# pip	9.0.1	9.0.2
# pytz	2018.3	2018.3
# requests	2.18.4	2.18.4
# ruamel.appconfig	0.5.3	0.5.3
# ruamel.std.argparse	0.8.1	0.8.1
# setuptools	28.8.0	39.0.1
# six	1.11.0	1.11.0
# urllib3	1.22	1.22

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
