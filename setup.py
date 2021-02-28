import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Notebook",
    version="0.0.1",
    author="Oleksandra Tsepilova",
    author_email="oleksandra.tsepilova@ucu.edu.ua",
    description="Console notebook aplication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sasha-tsepilova/notebook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)