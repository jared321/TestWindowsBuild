import codecs

from pathlib import Path
from setuptools import (
    setup, find_packages
)

_PKG_ROOT = Path(__file__).resolve().parent


def readme_rst():
    fname = _PKG_ROOT.joinpath("README.rst")
    with codecs.open(fname, encoding="utf8") as fptr:
        return fptr.read().replace("\n", "\r\n")


def version():
    fname = _PKG_ROOT.joinpath("VERSION")
    with open(fname, "r") as fptr:
        return fptr.read().strip()


python_requires = ">=3.9"
install_requires = []

package_data = {"mytest": []}

project_urls = {
    "Source": "https://github.com/jared321/TestWindowsBuild"
}

# This leads to \r\r\n line terminations in METADATA for Windows wheels built
# with a GH action
# long_description_content_type="text/x-rst",
setup(
    name="mytest",
    version=version(),
    author="My N. Ame",
    author_email="my@email.org",
    maintainer="My N. Ame",
    maintainer_email="my@email.org",
    description="Minimal reproducing example",
    long_description=readme_rst(),
    long_description_content_type="text/markdown",
    url="https://github.com/jared321/mytest",
    project_urls=project_urls,
    license="TBD",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data=package_data,
    python_requires=python_requires,
    install_requires=install_requires,
    keywords="mytest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
