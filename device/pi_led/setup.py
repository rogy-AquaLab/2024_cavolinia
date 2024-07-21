from setuptools import find_packages, setup

package_name = "pi_led"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="saho",
    maintainer_email="sahonorth@gmail.com",
    description="LEDを光らせる",
    license="MIT",
    entry_points={
        "console_scripts": [],
    },
)
