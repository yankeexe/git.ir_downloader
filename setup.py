""" Package setup. """
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "beautifulsoup4",
    "bleach",
    "certifi",
    "cffi",
    "chardet",
    "colorama",
    "cryptography",
    "cursor",
    "docutils",
    "halo",
    "idna",
    "importlib-metadata",
    "jeepney",
    "keyring",
    "log-symbols",
    "pkginfo",
    "pycparser",
    "Pygments",
    "readme-renderer",
    "requests",
    "requests-toolbelt",
    "SecretStorage",
    "six",
    "soupsieve",
    "spinners",
    "termcolor",
    "tqdm",
    "twine",
    "urllib3",
    "webencodings",
    "zipp"
]

# Development Requirements
requirements_dev = ["pytest<=4.*", "black<=19.10b0"]

setuptools.setup(
    name="gitir_downloader",
    version="0.0.6",
    author="Yankee Maharjan",
    author_email="yankee.exe@gmail.com",
    description="Download videos from scattered links of git.ir",
    url="https://github.com/yankeexe/gitir-downloader",
    license="MIT",
    packages=setuptools.find_packages("git.ir_downloader"),
    package_dir={"": "gitir_downloader"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    entry_points={"console_scripts": ["gid = gitir_downloader.main:start",]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
    ],
)
