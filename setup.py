from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='when_will_it_end',
    version = '0.0.2',
    packages=['when_will_it_end'],
    author="Zach Kurtz",
    author_email="zkurtz@gmail.com",
    description="A simpler progress monitor",
    url="https://github.com/zkurtz/when_will_it_end",
    license='MIT',
    long_description=long_description
)
