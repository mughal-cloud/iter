from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='Iter',
    version='0.1',
    description='Iter commands.',
    license="None",
    long_description=long_description,
    author='Zeeshan Mughal',
    author_email='zmughal89@gmail.com',
    url="http://www.zeeshanmughal.com/",
    packages=['iter'],
    install_requires=[],
    scripts=[]
)
