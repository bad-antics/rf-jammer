from setuptools import setup, find_packages
setup(name="rf-jammer", version="2.0.0", author="bad-antics", description="RF jamming detection and analysis toolkit", packages=find_packages(where="src"), package_dir={"":"src"}, python_requires=">=3.8")
