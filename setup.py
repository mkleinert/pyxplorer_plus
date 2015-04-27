from distutils.core import setup

setup(
    name='pyxplorer_plus',
    version='0.1.0',
    author='Martin Grund',
    author_email='grundprinzip+pip@gmail.com',
    packages=['pyxplorer_plus'],
    url='http://github.com/grundprinzip/pyxplorer_plus',
    license='LICENSE',
    description='Simple Big Data Profiling',
    long_description=open('README.rst').read(),
    install_requires=[
        "snakebite",
        "pyhs2",
        "pandas"
    ],
)
