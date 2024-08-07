import os
from glob import glob

from setuptools import find_packages, setup

package_name = "ul"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*")),
        ),
        (
            os.path.join("share", package_name, "config"),
            glob(os.path.join("config", "*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="h1rono",
    maintainer_email="hronok66@gmail.com",
    description="便利launchファイル集",
    license="MIT",
    tests_require=[],
    entry_points={
        "console_scripts": [],
    },
)
