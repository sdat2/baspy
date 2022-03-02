"""setup.py allows the installation of the project by pip."""
from setuptools import find_packages, setup

setup(
    name="baspy",
    version="1",
    author="Scott Hosking",
    url="https://github.com/sdat2/baspy",
    packages=find_packages(),
    # test_suite="src.tests.test_all.suite",
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest"],
)
