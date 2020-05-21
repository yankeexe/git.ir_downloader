""" Package setup. """
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["beautifulsoup4", "halo", "requests", "tqdm"]

# Development Requirements
requirements_dev = ["pytest<=4.*", "black<=19.10b0"]

setuptools.setup(
    name="gitir_download",
    version="1.0.1",
    author="Yankee Maharjan",
    author_email="yankee.exe@gmail.com",
    url="https://github.com/yankeexe/git.ir_downloader",
    description="Download videos from scattered links of git.ir",
    license="MIT",
    packages=setuptools.find_packages(exclude=["dist", "build", "*.egg-info"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    entry_points={"console_scripts": ["gid = gitir_downloader.main:start"]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
    ],
)
