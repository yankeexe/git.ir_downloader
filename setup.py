""" Package setup. """
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["requests==2.22.0", "beautifulsoup4==4.9.0", "pyfiglet==0.8.post1"]

# Development Requirements
requirements_dev = ["pytest==4.*", "black==19.10b0"]

setuptools.setup(
    name="git.ir downloader",
    version="0.0.1",
    author="Yankee Maharjan",
    description="Download videos from scattered links of git.ir",
    url="https://github.com/yankeexe/gitir-downloader",
    license="MIT",
    packages=setuptools.find_packages(
        where="scripts", exclude=["dist", "build", "*.egg-info"]
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
    ],
)
