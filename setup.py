from setuptools import setup

import versioneer

with open("requirements.txt") as reqs:
    REQUIREMENTS = [reqs.readlines()]

setup(
    name="sphinx_material",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Customized version of Material Sphinx theme by Kevin Sheppard (bashtage/sphinx-material)",
    long_description=open("README.rst").read(),
    author="Oğuz Ertan Ayanlar",
    author_email="oguzertanayanlar@gmail.com",
    url="https://github.com/OguzErtanAyanlarW/sphinx-material",
    packages=["sphinx_material"],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx :: Theme",
        "Topic :: Documentation :: Sphinx",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
