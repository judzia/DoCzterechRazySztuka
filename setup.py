import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="program",
    version=version,
    author="Julia Pawlik",
    author_email="Julia.m.p@interia.pl",
    description="Attendance management system for university",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/judzia/DoCzterechRazySztuka",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["DoCzterechRazySztuka=src.cli.cli:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        
    ],
    python_requires=">=3.9",
)