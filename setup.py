from setuptools import setup, find_namespace_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = [
]

setup(
    name="myterial",
    version="1.2.1",
    description="Easy acces to material colors hex codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    install_requires=requirements,
    extras_require={},
    python_requires=">=3.6",
    packages=find_namespace_packages(exclude=("tests, examples")),
    entry_points={},
    include_package_data=True,
    url="https://github.com/FedeClaudi/myterial",
    author="Federico Claudi",
    zip_safe=False,
)
