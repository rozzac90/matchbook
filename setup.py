
from setuptools import setup, find_packages
from matchbook import __version__

setup(
    name="matchbook",
    version=__version__,
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Matchbook API Python wrapper",
    url="https://github.com/rozzac90/matchbook",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open('README.rst').read(),
    tests_require=['pytest'],
)
