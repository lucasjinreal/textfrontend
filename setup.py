import os
import subprocess
import time
from setuptools import find_packages, setup
import io
from os import path


this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


version_file = "textfrontend/version.py"


def get_version():
    with open(version_file, "r") as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


if __name__ == "__main__":
    setup(
        name="textfrontend",
        version=get_version(),
        description="textfrontend: A Chinese TTS Training and Deploy Framework",
        long_description="",
        author="LucasJin",
        author_email="jinfagang19@163.com",
        keywords="computer vision, object detection",
        url="https://github.com/jinfagang/textfrontend",
        packages=find_packages(exclude=("configs", "tools", "demo", "images")),
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        license="Apache License 2.0",
        zip_safe=False,
    )
