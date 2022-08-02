from setuptools import find_namespace_packages, setup

project_packages = find_namespace_packages(include=["strivelogger", "strivelogger.*"])

setup(
    name="StriveLogger",
    version="0.0.1",
    packages=project_packages,
    package_data={
        "strivelogger": ["py.typed"],
    },
)
