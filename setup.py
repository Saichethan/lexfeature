import pathlib
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lexfeatures-SaichethanReddy", # Replace with your own username
    version="0.0.1",
    author="Saichethan M. Reddy",
    author_email="saichethanreddymiriyala@gmail.com",
    description="A wrapper for encoding Lexical features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Saichethan/lexfeature/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
